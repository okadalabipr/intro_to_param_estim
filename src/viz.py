def sim1(nth_paramset,sim,x,y0):
    search_idx = search_parameter_index()

    # get_best_param
    try:
        generation = np.load('./FitParam/%d/generation.npy'%(nth_paramset))
        best_indiv = np.load('./FitParam/%d/FitParam%d.npy'%(nth_paramset,int(generation)))

        for i in range(len(search_idx[0])):
            x[search_idx[0][i]] = best_indiv[i]
        for i in range(len(search_idx[1])):
            y0[search_idx[1][i]] = best_indiv[i+len(search_idx[0])]

    except:
        pass

    if sim.run_simulation(x,y0) is None:
        pass
    else:
        print('Simulation failed.\nparameter_set #%d'%(nth_paramset))

    return sim


def save_param_range(n_file):
    search_idx = search_parameter_index()
    search_param_matrix = np.empty((n_file,len(search_idx[0])))
    
    for nth_paramset in range(1,n_file+1):
        generation = np.load('./FitParam/%d/generation.npy'%(nth_paramset))
        best_indiv = np.load('./FitParam/%d/FitParam%d.npy'%(nth_paramset,int(generation)))
    
            
        search_param_matrix[nth_paramset-1,:] = best_indiv
    
    # ==========================================================================
    # seaborn.boxplot
    
    fig = plt.figure(figsize=(8,24))
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().yaxis.set_ticks_position('left')
    plt.gca().xaxis.set_ticks_position('bottom')
    
    ax = sns.boxplot(data=search_param_matrix,
                     orient='h',
                     linewidth=0.5,
                     palette='Set2'
                    )
    
    ax.set_xlabel('Parameter value')
    ax.set_ylabel('')
    ax.set_yticklabels([F_P[i] for i in search_idx[0]])
    ax.set_xscale('log')
    
    plt.savefig('./Fig/param_range.pdf',bbox_inches='tight')
    plt.close(fig)
    # ========================================================================== 
    

def viz(viz_type,show_all,stdev):
    x = f_params()
    y0 = initial_values()
    sim = Simulation(x,y0)

    n_file = 0
    fitparam_files = os.listdir('./FitParam')
    for file in fitparam_files:
        if re.match(r'\d',file):
            n_file += 1

    PMEK_cyt_all  = np.empty((n_file,len(sim.tspan),sim.condition))
    PERK_cyt_all  = np.empty((n_file,len(sim.tspan),sim.condition))
    PRSK_wcl_all  = np.empty((n_file,len(sim.tspan),sim.condition))
    PCREB_wcl_all = np.empty((n_file,len(sim.tspan),sim.condition))
    DUSPmRNA_all  = np.empty((n_file,len(sim.tspan),sim.condition))
    cFosmRNA_all  = np.empty((n_file,len(sim.tspan),sim.condition))
    cFosPro_all   = np.empty((n_file,len(sim.tspan),sim.condition))
    PcFos_all     = np.empty((n_file,len(sim.tspan),sim.condition))

    for i in range(n_file):
        sim = sim1(i+1,sim,x,y0)

        PMEK_cyt_all[i,:,:]  = sim.PMEK_cyt
        PERK_cyt_all[i,:,:]  = sim.PERK_cyt
        PRSK_wcl_all[i,:,:]  = sim.PRSK_wcl
        PCREB_wcl_all[i,:,:] = sim.PCREB_wcl
        DUSPmRNA_all[i,:,:]  = sim.DUSPmRNA
        cFosmRNA_all[i,:,:]  = sim.cFosmRNA
        cFosPro_all[i,:,:]   = sim.cFosPro
        PcFos_all[i,:,:]     = sim.PcFos

    best_fitness_all = np.empty(n_file)
    for i in range(n_file):
        if os.path.isfile('./FitParam/%d/BestFitness.npy'%(i+1)):
            best_fitness_all[i] = np.load('./FitParam/%d/BestFitness.npy'%(i+1))
        else:
            best_fitness_all[i] = np.inf

    global best_paramset
    best_paramset = np.argmin(best_fitness_all) + 1

    sim = sim1(int(best_paramset),sim,x,y0)

    save_param_range(n_file)

    plot_func(sim,n_file,viz_type,show_all,stdev,
        PMEK_cyt_all,
        PERK_cyt_all,
        PRSK_wcl_all,
        PCREB_wcl_all,
        DUSPmRNA_all,
        cFosmRNA_all,
        cFosPro_all,
        PcFos_all
    )