from pathlib import Path
import yaml


QUESTION = "Where should a deduplicated_events artifact be inserted in this pipeline?"


def load_artifacts(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)["artifacts"]


def score_artifact(artifact, question):
    name = artifact["name"]
    purpose = artifact.get("purpose", "")
    text = f"{name} {purpose}".lower()

    score = 0
    reasons = []

    if name == "raw_events":
        score += 5
        reasons.append("source artifact where duplicates may originate")

    if name == "normalized_events":
        score += 4
        reasons.append("first downstream artifact affected by duplicate removal")

    if name == "feature_table":
        score += 3
        reasons.append("feature extraction may be distorted by duplicates")

    if name == "summary_table":
        score += 1
        reasons.append("downstream output affected by earlier aggregation")

    if "duplicate" in question.lower():
        score += 1
        reasons.append("question concerns duplicate handling")

    return score, reasons


def select_artifacts(question, artifacts, min_score=1):
    selected = []

    for artifact in artifacts:
        score, reasons = score_artifact(artifact, question)
        if score >= min_score:
            selected.append(
                {
                    "name": artifact["name"],
                    "score": score,
                    "reasons": reasons,
                }
            )

    return sorted(selected, key=lambda item: item["score"], reverse=True)


def build_context_packet(question, artifacts, selected):
    selected_names = {item["name"] for item in selected}
    selected_by_name = {item["name"]: item for item in selected}

    packet_artifacts = []

    for artifact in artifacts:
        name = artifact["name"]

        if name not in selected_names:
            continue

        selection = selected_by_name[name]

        packet_artifacts.append(
            {
                "name": name,
                "score": selection["score"],
                "reasons": selection["reasons"],
                "purpose": artifact.get("purpose", ""),
                "path": artifact.get("path", ""),
                "depends_on": artifact.get("depends_on", []),
            }
        )

    return {
        "question": question,
        "artifacts": packet_artifacts,
        "proposed_artifact": {
            "name": "deduplicated_events",
            "depends_on": ["raw_events"],
            "feeds_into": ["normalized_events"],
        },
    }


def print_selected_artifacts(selected):
    print("Selected artifacts:")

    for item in selected:
        print(f"- {item['name']} (score: {item['score']})")
        for reason in item["reasons"]:
            print(f"  - {reason}")


def print_context_packet(packet):
    print("\nContext packet:\n")
    print(f"Question: {packet['question']}\n")

    for artifact in packet["artifacts"]:
        print(f"- {artifact['name']}")
        print(f"  purpose: {artifact['purpose']}")
        print(f"  path: {artifact['path']}")
        print(f"  depends_on: {artifact['depends_on']}")
        print(f"  selected because:")
        for reason in artifact["reasons"]:
            print(f"    - {reason}")
        print()

    proposed = packet["proposed_artifact"]

    print("Proposed artifact:")
    print(f"- {proposed['name']}")
    print(f"  depends_on: {proposed['depends_on']}")
    print(f"  feeds_into: {proposed['feeds_into']}")


def main():
# Hypothetical scenario: assume deduplicated_events does not yet exist
    artifacts = [
        artifact
        for artifact in load_artifacts(Path("artifacts.yaml"))
        if artifact["name"] != "deduplicated_events"
    ]
    selected = select_artifacts(QUESTION, artifacts)
    packet = build_context_packet(QUESTION, artifacts, selected)

    print(f"Question: {QUESTION}\n")
    print_selected_artifacts(selected)
    print_context_packet(packet)


if __name__ == "__main__":
    main()
