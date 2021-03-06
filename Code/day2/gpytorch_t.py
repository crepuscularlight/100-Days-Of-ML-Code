import math
import torch
import gpytorch
from matplotlib import pyplot as plt


train_x=torch.linspace(0,1,100)
train_y=torch.sin(2*math.pi*train_x)+torch.randn(train_x.size())*math.sqrt(0.04)

# class ExactGPModel(gpytorch.models.ExactGP):
#     def __init__(self, train_x, train_y, likelihood):
#         super(ExactGPModel, self).__init__(train_x, train_y, likelihood)
#         self.mean_module = gpytorch.means.ConstantMean()
#         self.covar_module = gpytorch.kernels.ScaleKernel(gpytorch.kernels.RBFKernel())

#     def forward(self, x):
#         mean_x = self.mean_module(x)
#         covar_x = self.covar_module(x)
#         return gpytorch.distributions.MultivariateNormal(mean_x, covar_x)

# # initialize likelihood and model
# likelihood = gpytorch.likelihoods.GaussianLikelihood()
# model = ExactGPModel(train_x, train_y, likelihood)
class ExactGPModel(gpytorch.models.ExactGP): 
    def __init__(self,train_x,train_y,likelihood):
        super(ExactGPModel, self).__init__(train_x,train_y,likelihood)
        self.mean_module=gpytorch.means.ConstantMean()
        self.covar_module=gpytorch.kernels.ScaleKernel(gpytorch.kernels.RBFKernel())
        
    def forward(self,x):
        mean_x=self.mean_module(x)
        covar_x=self.covar_module(x)
        return gpytorch.distributions.MultivariateNormal(mean_x,covar_x)
    
#     # initialize likelihood and model
# likelihood = gpytorch.likelihoods.GaussianLikelihood()
# model = ExactGPModel(train_x, train_y, likelihood)
# def main():
#     likelihood=gpytorch.likelihoods.GaussianLikelihood()
#     model=ExactGPModel(train_x,train_y,likelihood)
#     # Find optimal model hyperparameters
#     model.train()
#     likelihood.train()

#     # Use the adam optimizer
#     optimizer = torch.optim.Adam(model.parameters(), lr=0.1)  # Includes GaussianLikelihood parameters

#     # "Loss" for GPs - the marginal log likelihood
#     mll = gpytorch.mlls.ExactMarginalLogLikelihood(likelihood, model)
#     training_iter=50
#     for i in range(training_iter):
#         # Zero gradients from previous iteration
#         optimizer.zero_grad()
#         # Output from model
#         output = model(train_x)
#         # Calc loss and backprop gradients
#         loss = -mll(output, train_y)
#         loss.backward()
#         print('Iter %d/%d - Loss: %.3f   lengthscale: %.3f   noise: %.3f' % (
#             i + 1, training_iter, loss.item(),
#             model.covar_module.base_kernel.lengthscale.item(),
#             model.likelihood.noise.item()
#         ))
#         optimizer.step()
#     model.eval()
#     likelihood.eval()

#     # Test points are regularly spaced along [0,1]
#     # Make predictions by feeding model through likelihood
#     with torch.no_grad(), gpytorch.settings.fast_pred_var():
#         test_x = torch.linspace(0, 1, 51)
#         observed_pred = likelihood(model(test_x))
#     with torch.no_grad():
#         # Initialize plot
#         f, ax = plt.subplots(1, 1, figsize=(4, 3))

#         # Get upper and lower confidence bounds
#         lower, upper = observed_pred.confidence_region()
#         # Plot training data as black stars
#         ax.plot(train_x.numpy(), train_y.numpy(), 'k*')
#         # Plot predictive means as blue line
#         ax.plot(test_x.numpy(), observed_pred.mean.numpy(), 'b')
#         # Shade between the lower and upper confidence bounds
#         ax.fill_between(test_x.numpy(), lower.numpy(), upper.numpy(), alpha=0.5)
#         ax.set_ylim([-3, 3])
#         ax.legend(['Observed Data', 'Mean', 'Confidence'])
#         plt.show()
#         print("hi")
# if __name__ == '__main__':
#     main()
    
def main():
    likelihood=gpytorch.likelihoods.GaussianLikelihood()
    model=ExactGPModel(train_x,train_y,likelihood)
    # model.train()
    # print("-----1-----",model.train())
    # likelihood.train()
    #     # Use the adam optimizer
    optimizer = torch.optim.Adam(model.parameters(), lr=0.1)  # Includes GaussianLikelihood parameters

    # "Loss" for GPs - the marginal log likelihood
    mll = gpytorch.mlls.ExactMarginalLogLikelihood(likelihood, model)
    training_iter=50
    for i in range(training_iter):
        # Zero gradients from previous iteration
        optimizer.zero_grad()
        # Output from model
        output = model(train_x)
        # Calc loss and backprop gradients
        loss = -mll(output, train_y)
        loss.backward()
        print('Iter %d/%d - Loss: %.3f   lengthscale: %.3f   noise: %.3f' % (
            i + 1, training_iter, loss.item(),
            model.covar_module.base_kernel.lengthscale.item(),
            model.likelihood.noise.item()
        ))
        optimizer.step()
    model.eval()
    # print("-----2-----",model.eval())
    likelihood.eval()
    with torch.no_grad(), gpytorch.settings.fast_pred_var():
        test_x = torch.linspace(0, 1, 51)
        observed_pred = likelihood(model(test_x))
    
    with torch.no_grad():
        f,ax=plt.subplots(1,1,figsize=(10,10))
        lower,upper=observed_pred.confidence_region()
        ax.plot(train_x.numpy(),train_y.numpy(),'k*')
        ax.plot(test_x.numpy(),observed_pred.mean.numpy(),'')
        ax.plot(test_x.numpy(),model(test_x).mean.numpy(),'ro')
        ax.fill_between(test_x.numpy(), lower.numpy(), upper.numpy(), alpha=0.5)
        ax.set_ylim([-3, 3])
        ax.legend(['Observed Data', 'Mean', 'Confidence'])
        plt.show()
        

if __name__ == '__main__':
    main()