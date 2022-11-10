import pandas as pd
import numpy as np
import os

columns = ['input_image_url', 'mask_url', 'image_A_url', 'image_B_url', 'image_C_url', 'text']

input_urls = []
mask_urls = []
A_urls = []
B_urls = []
C_urls = []


for fname in sorted(os.listdir('input')):
	if fname.endswith(('.jpg', '.jpeg', 'png')):
		input_urls += ['https://raw.githubusercontent.com/veroveroxie/user_study/main/input/'+fname]

for fname in sorted(os.listdir('masks')):

	if fname.endswith(('.jpg', '.jpeg', 'png')):
		mask_urls += ['https://raw.githubusercontent.com/veroveroxie/user_study/main/masks/'+fname]

for fname in sorted(os.listdir('dalle2')):
	if fname.endswith(('.jpg', '.jpeg', 'png')):
		A_urls += ['https://raw.githubusercontent.com/veroveroxie/user_study/main/dalle2/'+fname]

for fname in sorted(os.listdir('ours')):
	if fname.endswith(('.jpg', '.jpeg', 'png')):
		B_urls += ['https://raw.githubusercontent.com/veroveroxie/user_study/main/ours/'+fname]

for fname in sorted(os.listdir('stable_inpainting')):
	if fname.endswith(('.jpg', '.jpeg', 'png')):
		C_urls += ['https://raw.githubusercontent.com/veroveroxie/user_study/main/stable_inpainting/'+fname]


df = pd.DataFrame()
df['input_image_url'] = input_urls
df['mask_url'] = mask_urls
df['image_A_url'] = A_urls
df['image_B_url'] = B_urls
df['image_C_url'] = C_urls


descs = ['']

df['descriptions'] = descs

df.to_csv('my_dict.csv', index=False)



		
