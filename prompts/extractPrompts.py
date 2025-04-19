import sys
import json

path = "human-eval-v2-20210705.jsonl"
prompts = []

with open(path, 'r') as file:
    for line in file:
        prompt = json.loads(line)
        prompts.append({ "task_id": prompt["task_id"], "prompt": prompt["prompt"] })

with open('prompts.json', 'w') as f:
    json.dump(prompts, fp=f, indent=2)
