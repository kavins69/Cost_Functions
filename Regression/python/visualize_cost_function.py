import numpy as np
import matplotlib.pyplot as plt
x=np.array([1,2,3,4])
y=np.array([2,3,4,6])

def gradient_descent(x,y):
    m_curr=b_curr=0
    iteration=10000
    lr=0.0001
    n=len(x)

    plt.ion()
    fig, ax = plt.subplots()
    fig2, ax2 = plt.subplots()

    for i in range(iteration):
        y_pred=m_curr*x+b_curr
        md = -(2 / n) * (sum(x * (y - y_pred)))
        bd = -(2 / n) * (sum(y - y_pred))
        m_curr = m_curr - lr * md
        b_curr = b_curr - lr * bd
        cost_fn=(1/n)*(sum(y-y_pred)** 2)
        if i % 50 == 0:
            ax.clear()
            ax.scatter(x, y, color="red", label="Data Points")
            ax.plot(x, y_pred, color="blue", label=f"Iteration {i}")
            ax.set_title(f"Iteration {i}: m={m_curr:.2f}, b={b_curr:.2f}")
            ax.legend()
            plt.pause(0.1)

        print("m= {} b= {} cost_fn= {} iter= {}".format(m_curr,b_curr,cost_fn,i))
    plt.ioff()
    plt.show()


gradient_descent(x,y)