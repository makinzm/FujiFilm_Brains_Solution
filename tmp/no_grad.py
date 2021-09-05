import torch

x = torch.tensor([1.0], requires_grad=True)

with torch.no_grad():
    y = x * 2
print(y.requires_grad)

torch.no_grad()
z=x**2
print(z.requires_grad)
