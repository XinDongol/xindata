import time
import torch
import torchvision.transforms as transforms
import torch.utils.data as data
from torchvision.datasets import ImageFolder


transform_train = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
])

datadir = '/scratch/tiny-imagenet-200'
# datadir = '/n/holyscratch01/kung_lab/xin/xindata/tinyimagenet/tiny-imagenet-200'

train_ds = ImageFolder(datadir+'/train/', transform=transform_train)

train_dl = data.DataLoader(dataset=train_ds, 
                           batch_size=64, 
                           drop_last=False, 
                           shuffle=True, 
                           num_workers=2)

start_time = time.time()

for idx, (data, label) in enumerate(train_dl):
    if idx==0:
        print(data.size())


print((time.time()-start_time)/(idx+1))


