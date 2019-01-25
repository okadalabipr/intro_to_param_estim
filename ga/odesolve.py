from scipy.integrate import ode

def odesolve(diffeq,y0,tspan,tuple_x):
    sol = ode(diffeq)
    sol.set_integrator('vode',method='bdf',min_step=1e-8,with_jacobian=True)
    sol.set_initial_value(y0,tspan[0])
    sol.set_f_params(tuple_x)

    T = [tspan[0]]
    Y = [y0]

    while sol.successful() and sol.t < tspan[-1]:
        #sol.integrate(tspan[-1],step=True)
        sol.integrate(sol.t+1.)
        T.append(sol.t)
        Y.append(sol.y)

    return np.array(T),np.array(Y)
