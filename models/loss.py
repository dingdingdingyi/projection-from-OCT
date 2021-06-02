import torch.nn as nn
import torch.nn.functional as F
import torch
import numpy as np
from torch.autograd import Variable

class MaxPoolLoss(nn.Module):
    def __init__(self, height=10, weight=400):
        super(MaxPoolLoss, self).__init__()
        self.height = height
        self.weight = weight

    def forward(self, max, target):
        # assert predict.shape[0] == target.shape[0], "predict & target batch size don't match"
        # batch_size = input.size(0)
        # first_line = (predict[:,:,0,:]*640 - 320)/320
        # second_line = ((predict[:,:,0,:] + 0.5*predict[:,:,1,:])*640 -320)/320
        # line = torch.cat((first_line.unsqueeze(3), second_line.unsqueeze(3)),3)
        # predict = F.interpolate(line, size=[self.height, self.weight], mode='bilinear', align_corners=True)
        # # predict = (predict*640 - 320)/320
        # predict = predict.squeeze(1)
        # grid = torch.zeros((batch_size, self.height, self.weight, 2), requires_grad=True).to(device)
        # grid[:,:,:,1] = predict
        # grid[:,:,:,0] = torch.linspace(-1, 1, steps=400)
        # outp = torch.zeros((batch_size, 3, self.height, self.weight), requires_grad=True).to(device)
        # outp = F.grid_sample(input , grid, mode='bilinear', padding_mode='zeros', align_corners=True)
        # max = torch.zeros((batch_size, 3, self.weight), requires_grad=True).to(device)
        # max, index = torch.max(outp, dim=2, keepdim=False, out=None)
        # max = max.unsqueeze(dim=2).to(device)
        # max = Variable(max,requires_grad=True).cuda()
        loss = F.smooth_l1_loss(max, target)

        return loss
    # def forward(self, predict, target):
    #     first_line = (predict[:,:,0,:]*640 - 320)/320
    #     second_line = ((predict[:,:,0,:] + 0.5*predict[:,:,1,:])*640 -320)/320
    #     line = torch.cat((first_line.unsqueeze(3), second_line.unsqueeze(3)),3)
    #     print(line.shape)
    #     # predict = torch.nn.functional.upsample_bilinear(predict, size=[self.height, self.weight])
    #     # # print(predict)
    #     # predict = predict * 255
    #     # # print(predict,target[:,0,:,:])
    #     # loss = F.smooth_l1_loss(predict, target[:,0,:,:].unsqueeze(1))
    #     # # print(loss.requires_grad)
    #     return line