import os
from PIL import Image
import json
import re

input_folder = "./"
output_file = "meta_prompts.txt"
clean_output = "clean_meta_prompts.txt"
prompts = set()

with open(output_file, "w") as f, open(clean_output, 'w') as cf:
    for root, dirs, files in os.walk(input_folder):
        for filename in files:
            if filename.endswith(".png"):
                filepath = os.path.join(root, filename)
                try:
                    with Image.open(filepath) as im:
                        metadata = im.info
                        json_string = json.dumps(metadata)
                        data = json.loads(json_string)
                        prompt = data['parameters'].split('Negative prompt:')[0].split('Steps:')[0].replace("\n"," ").strip()
                        #prompt = re.sub(r'Steps: \d+, Sampler: [a-zA-Z0-9 ]+, CFG scale: \d+, Seed: \d+, Size: \d+x\d+, Model hash: [a-zA-Z0-9]+, Model: [a-zA-Z0-9()\[\]]+, Denoising strength: \d+\.\d+, Mask blur: \d+', '', prompt)
                        prompt = prompt.strip()
                        clean_prompt = re.sub(r'<.*?>', '', prompt).strip()

                        if prompt not in prompts:
                            prompts.add(prompt)
                            f.write(prompt + '\n')
                            if clean_prompt:
                                cf.write(clean_prompt + '\n')
                except:
                    print(f"Error processing file {filename}")