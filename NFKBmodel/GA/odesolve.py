from scipy.integrate import ode
def odesolve(DIFFEQ,Y_ZERO,TSPAN,ARGS):
    sol = ode(DIFFEQ)
    sol.set_integrator('vode',method='bdf',min_step=1e-8,with_jacobian=True)
    sol.set_initial_value(Y_ZERO,TSPAN[0])
    sol.set_f_params(ARGS)

    T = [TSPAN[0]]
    Y = [Y_ZERO]

    while sol.successful() and sol.t < TSPAN[-1]:
        #sol.integrate(TSPAN[-1],step=True)
        sol.integrate(sol.t+1.)
        T.append(sol.t)
        Y.append(sol.y)

    return np.array(T),np.array(Y)
