import torch
import torchvision
import torchvision.transforms as transforms
import torch.optim as optim
import torch.nn as nn
import torch.nn.functional as F
import matplotlib.pyplot as plt
import numpy as np

class CNNData:
    def __init__(self):
        self.train_loader = None
        self.test_loader = None
        self.classes = ('plane', 'car', 'bird', 'cat',
                'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

    def get_classes(self):
        return self.classes

    def load_data_set(self):
        transform = self.__transform_to_tensor()
        batch_size = 4
        trainset = torchvision.datasets.CIFAR10(root='./data', train=True,
                                                download=True, transform=transform)
        self.train_loader = torch.utils.data.DataLoader(trainset, batch_size=batch_size,
                                                shuffle=True, num_workers=2)

        testset = torchvision.datasets.CIFAR10(root='./data', train=False,
                                            download=True, transform=transform)
        self.test_loader = torch.utils.data.DataLoader(testset, batch_size=batch_size,
                                                shuffle=False, num_workers=2)
    def get_loader(self, type):
        if type == 'train': 
            return self.train_loader 
        return self.test_loader

    def __transform_to_tensor(self):
        transform = transforms.Compose(
            [transforms.ToTensor(),
                transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))]
        )
        return transform

class ImgClass:
    def __init__(self):
        pass

    def imgshow(self, img):
        img = img / 2 + 0.5
        npimg = img.numpy()
        plt.imgshow(np.transpose(npimg, (1,2,0)))
        plt.show()

class CNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)
    
    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = torch.flatten(x, 1)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x
    

class ModelTrainer:
    def __init__(self, train_data=None, test_data=None, model=None):
        self.train_data = train_data
        self.test_data = test_data
        self.model = model
    
    def train_model(self,num_epochs=2, device='cuda:0'):
        criterion = nn.CrossEntropyLoss()
        optimizer = optim.SGD(self.model.parameters(), lr=0.001, momentum=0.9)
        for epoch in range(num_epochs):
            running_loss = 0.0
            for i, dta in enumerate(self.data, 0):
                inputs, labels = dta[0].to(device), dta[1].to(device)

                optimizer.zero_grad()

                #forward + backward + optimize
                outputs = self.model(inputs)
                loss = criterion(outputs, labels)
                loss.backward()
                optimizer.step()

                #print stats
                running_loss += loss.item()
                if i % 2000 == 1999: #print every 2000 mini-batches
                    print(f'[{epoch + 1}, {i + 1:5d}] loss: {running_loss / 2000:.3f}')
                    running_loss = 0.0

        print("Completed training")

    def test_model(self, classes, load_model=True, device='cuda:0'):
        if load_model:
            self.model = self.load_torch_model()
        # prepare to count predictions for each class
        correct_pred = {classname: 0 for classname in classes}
        total_pred = {classname: 0 for classname in classes}

        # again no gradients needed
        with torch.no_grad():
            for data in self.test_data:
                images, labels = data[0].to(device), data[1].to(device)
                outputs = self.model(images)
                _, predictions = torch.max(outputs, 1)
                # collect the correct predictions for each class
                for label, prediction in zip(labels, predictions):
                    if label == prediction:
                        correct_pred[classes[label]] += 1
                    total_pred[classes[label]] += 1


        # print accuracy for each class
        for classname, correct_count in correct_pred.items():
            accuracy = 100 * float(correct_count) / total_pred[classname]
            print(f'Accuracy for class: {classname:5s} is {accuracy:.1f} %')

    def save_torch_file(self):
        PATH = "path"
        torch.save(self.model.state_dict(), PATH)
    
    def load_torch_model(self, model_path="path"):
        net = self.model
        net.load_state_dict(torch.load(model_path))
        return net


"""
# get some random training images
dataiter = iter(trainloader)
images, labels = next(dataiter)

# show images
imshow(torchvision.utils.make_grid(images))
# print labels
print(' '.join(f'{classes[labels[j]]:5s}' for j in range(batch_size)))
"""
def train_network():
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    cnn_data = CNNData()
    cnn_data.load_data_set()
    train_data = cnn_data.get_loader("train")
    test_data = cnn_data.get_loader("test")
    net = CNN()
    classes = cnn_data.get_classes()
    net.to(device)
    model_training = ModelTrainer(train_data, test_data, net)
    model_training.test_model(classes, load_model=True)

if __name__ == "__main__":
    train_network()