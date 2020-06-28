import numpy as np
from matplotlib import pyplot as plt

def estimate_coeff(x,y):
    n=np.size(x)
    sumofx=np.sum(x)
    sumofy=np.sum(y)
    sumofxsq=np.sum(x*x)
    sumofxy=np.sum(x*y)
    print("Sum 0f x =",sumofx)
    print("Sum 0f y =",sumofy)
    print("Sum of x sqr =",sumofxsq)
    print("Sum of xy =",sumofxy)
    slope=(n*sumofxy-sumofx* sumofy)/(n*sumofxsq-sumofx**2)
    y_intercept=(sumofy *sumofxsq-sumofx*sumofxy)/(n*sumofxsq-sumofx**2)
    return [slope,y_intercept]

def plot_regression_line(x,y,b):
    plt.scatter(x,y,color="r",marker="o",s=30)
    y_pred=b[1]*x+b[0]
    plt.scatter(x,y_pred,color="g",marker="*")
    plt.plot(x,y_pred,color="b")
    plt.xticks(np.arange(0,11,1))
    plt.yticks(np.arange(0,25,3))
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

def predict(slope,y_intercept,input_x):
    predict_y=slope*input_x+y_intercept
    return(predict_y)

def main():
    x=np.array([0,1,2,3,4,5,6,7,8,9])
    y=np.array([3,5,7,9,12,16,15,18,19,21])
    slope,y_intercept=estimate_coeff(x,y)
    print("Estmate coeff:\n")
    print("slope m=",slope)
    print("y-intercept c=",y_intercept)
    plot_regression_line(x,y,[y_intercept,slope])

    x_input=eval(input("Enter the value of x:"))
    predicted_y=predict(slope,y_intercept,x_input)
    print("predicted-y:",predicted_y)
