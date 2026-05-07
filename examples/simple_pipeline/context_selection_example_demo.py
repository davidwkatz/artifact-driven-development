from pathlib import Path
import yaml


QUESTION = "Why does this pipeline perform duplicate removal before feature extraction?"


def load_artifacts(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)["artifacts"]


def score_artifact(artifact, question):
    name = artifact["name"]
    purpose = artifact.get("purpose", "")
    text = f"{name} {purpose}".lower()

    score = 0
    reasons = []

    if name == "deduplicated_events":
        score += 5
        reasons.append("focal artifact for duplicate removal")

    if name == "raw_events":
        score += 3
        reasons.append("upstream source where duplicate events may originate")

    if name == "normalized_events":
        score += 3
        reasons.append("cleaned layer affected by deduplication")

    if name == "feature_table":
        score += 3
        reasons.append("feature extraction depends on cleaned event records")

    if name == "summary_table":
        score += 1
        reasons.append("downstream output useful for checking impact")

    if "duplicate" in question.lower() and "duplicate" in text:
        score += 1
        reasons.append("artifact metadata mentions duplicate handling")

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


def main():
    artifacts = load_artifacts(Path("artifacts.yaml"))

    selected = select_artifacts(QUESTION, artifacts)
    packet = build_context_packet(QUESTION, artifacts, selected)

    print(f"Question: {QUESTION}\n")
    print_selected_artifacts(selected)
    print_context_packet(packet)


if __name__ == "__main__":
    main()
