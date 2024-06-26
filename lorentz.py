import numpy as np
import matplotlib.pyplot as plt
import random
import tqdm

class LorentzAttractor:
    def __init__(self,sigma:float = 1.0,rho:float= 1.0,beta:float=1.0, N:int=100, start_conditions:dict = {
        "x" : 0.0,
        "y" : 0.0,
        "z" : 0.0}) -> None:
        self.N = N
        self.sigma = sigma
        self.rho = rho
        self.beta = beta
        self.x, self.y, self.z = start_conditions["x"], start_conditions["y"], start_conditions["z"]
    

    def plot(self):
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        plt.title(f"Initial Conditions: {(self.x, self.y, self.z)}")
        # ax.axes.set_xlim3d(left=-100, right=100) 
        # ax.axes.set_ylim3d(bottom=-100, top=100) 
        # ax.axes.set_zlim3d(bottom=-100, top=100) 
        x,y,z = [],[],[]
        for _ in tqdm.tqdm(range(self.N)):
            x.append(self.x)
            y.append(self.y)
            z.append(self.z)
            dt = 1e-4
            dx = (self.sigma * (self.y - self.x))*dt
            dy = (self.x * self.rho - self.x * self.z -  self.y)*dt
            dz = ((self.x * self.y) - (self.beta*self.z))*dt
            self.x += dx
            self.y += dy
            self.z += dz
        
        ax.plot3D(x,y,z, "-o")
        plt.show()


if __name__ == "__main__":
    """
    N:int == The number of points to plot
    sigma: float == The sigma constant representation found in Lorentz Attractor
    rho: float == The rho constant representation found in Lorentz Attractor
    beta: float == The beta constant representation found in Lorentz Attractor
    initial_conditions:dict == Dictionary containing randomized perturbed initial conditions
    """
    initial_conditions = {
        "x":random.uniform(0,10),
        "y":random.uniform(0,10),
        "z":random.uniform(0,10)
    }
    set_val = int(input("Hello! Please enter the number of points you would like to simulate. Single core processors are not recommended to use values >1e8.\n"))
    use_def = bool(input("Would you like to use the default Lorentz constant parameters? Enter 1 for yes, 2 for no.\n"))
    if use_def:
        lorentz = LorentzAttractor(N=set_val, sigma=10.0, rho = 28, beta=2.667, start_conditions=initial_conditions)
        lorentz.plot()
    else:
        user_sigma = float(input("Please enter the sigma constant value:\n"))
        user_rho = float(input("Please enter the rho constant value:\n"))
        user_beta = float(input("Please enter the beta constant value:\n"))
        lorentz = LorentzAttractor(N=set_val, sigma=user_sigma, rho = user_rho, beta=user_beta, start_conditions=initial_conditions)
        lorentz.plot()

