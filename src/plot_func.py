def plot_func(sim,n_file,viz_type,show_all,stdev,
    PMEK_cyt_all,
    PERK_cyt_all,
    PRSK_wcl_all,
    PCREB_wcl_all,
    DUSPmRNA_all,
    cFosmRNA_all,
    cFosPro_all,
    PcFos_all
    ):

    exp = ExperimentalData()

    plt.figure(figsize=(20,8))
    plt.rcParams['font.size'] = 16
    plt.rcParams['font.family'] = 'Arial'
    plt.rcParams['axes.linewidth'] = 2
    plt.rcParams['lines.linewidth'] = 2.5
    plt.rcParams['lines.markersize'] = 10
    plt.subplots_adjust(wspace=0.5, hspace=0.5)

    plt.subplot(2,4,1)
    plt.plot(sim.t,sim.PMEK_cyt[:,0],'b')
    plt.plot(sim.t,sim.PMEK_cyt[:,1],'r')

    e = plt.errorbar(exp.t2/60.,exp.egf_MEKc_av,yerr=exp.egf_MEKc_se,lw=1,
        markerfacecolor='None',markeredgecolor='b',fmt='bD',capsize=8,clip_on=False)
    for b in e[1]:
        b.set_clip_on(False)
    e = plt.errorbar(exp.t2/60.,exp.hrg_MEKc_av,yerr=exp.hrg_MEKc_se,lw=1,
        markerfacecolor='None',markeredgecolor='r',fmt='rs',capsize=8,clip_on=False)
    for b in e[1]:
        b.set_clip_on(False)
    plt.xlim(0,90)
    plt.xticks([0,30,60,90])
    plt.yticks([0,0.2,0.4,0.6,0.8,1,1.2])
    plt.ylim(0,1.2)
    plt.xlabel('Time (min)')
    plt.ylabel('Phosphorylated MEK\n(cytoplasm)')


    plt.subplot(2,4,2)
    if show_all:
        for i in range(n_file):
            plt.plot(sim.t,PERK_cyt_all[i,:,0]/np.max(PERK_cyt_all[i,:,:]),'b',alpha=0.05)
            plt.plot(sim.t,PERK_cyt_all[i,:,1]/np.max(PERK_cyt_all[i,:,:]),'r',alpha=0.05)

    if not viz_type == 'average':
        plt.plot(sim.t,sim.PERK_cyt[:,0]/np.max(sim.PERK_cyt[:,1]),'b')
        plt.plot(sim.t,sim.PERK_cyt[:,1]/np.max(sim.PERK_cyt[:,1]),'r')
    else:
        PERK_cyt_norm  = np.empty((n_file,len(sim.tspan),sim.condition))
        for i in range(n_file):
            PERK_cyt_norm[i,:,0] = PERK_cyt_all[i,:,0]/np.max(PERK_cyt_all[i,:,:])
            PERK_cyt_norm[i,:,1] = PERK_cyt_all[i,:,1]/np.max(PERK_cyt_all[i,:,:])
        plt.plot(sim.t,np.average(PERK_cyt_norm[:,:,0],axis=0),'b')
        plt.plot(sim.t,np.average(PERK_cyt_norm[:,:,1],axis=0),'r')
        if stdev:
            plt.errorbar(sim.t,np.average(PERK_cyt_norm[:,:,0],axis=0),
                yerr=[np.std(PERK_cyt_norm[:,i,0],ddof=1) for i in range(len(sim.t))],
                fmt='None',ecolor='b',lw=0.05,alpha=0.1)
            plt.errorbar(sim.t,np.average(PERK_cyt_norm[:,:,1],axis=0),
                yerr=[np.std(PERK_cyt_norm[:,i,1],ddof=1) for i in range(len(sim.t))],
                fmt='None',ecolor='r',lw=0.05,alpha=0.1)

    e = plt.errorbar(exp.t2/60.,exp.egf_ERKc_av,yerr=exp.egf_ERKc_se,lw=1,
        markerfacecolor='None',markeredgecolor='b',fmt='bD',capsize=8,clip_on=False)
    for b in e[1]:
        b.set_clip_on(False)
    e = plt.errorbar(exp.t2/60.,exp.hrg_ERKc_av,yerr=exp.hrg_ERKc_se,lw=1,
        markerfacecolor='None',markeredgecolor='r',fmt='rs',capsize=8,clip_on=False)
    for b in e[1]:
        b.set_clip_on(False)
    plt.xlim(0,90)
    plt.xticks([0,30,60,90])
    plt.yticks([0,0.2,0.4,0.6,0.8,1,1.2])
    plt.ylim(0,1.2)
    plt.xlabel('Time (min)')
    plt.ylabel('Phosphorylated ERK\n(cytoplasm)')


    plt.subplot(2,4,3)
    if show_all:
        for i in range(n_file):
            plt.plot(sim.t,PRSK_wcl_all[i,:,0]/np.max(PRSK_wcl_all[i,:,:]),'b',alpha=0.05)
            plt.plot(sim.t,PRSK_wcl_all[i,:,1]/np.max(PRSK_wcl_all[i,:,:]),'r',alpha=0.05)

    if not viz_type == 'average':
        plt.plot(sim.t,sim.PRSK_wcl[:,0]/np.max(sim.PRSK_wcl[:,1]),'b')
        plt.plot(sim.t,sim.PRSK_wcl[:,1]/np.max(sim.PRSK_wcl[:,1]),'r')
    else:
        PRSK_wcl_norm  = np.empty((n_file,len(sim.tspan),sim.condition))
        for i in range(n_file):
            PRSK_wcl_norm[i,:,0] = PRSK_wcl_all[i,:,0]/np.max(PRSK_wcl_all[i,:,:])
            PRSK_wcl_norm[i,:,1] = PRSK_wcl_all[i,:,1]/np.max(PRSK_wcl_all[i,:,:])
        plt.plot(sim.t,np.average(PRSK_wcl_norm[:,:,0],axis=0),'b')
        plt.plot(sim.t,np.average(PRSK_wcl_norm[:,:,1],axis=0),'r')
        if stdev:
            plt.errorbar(sim.t,np.average(PRSK_wcl_norm[:,:,0],axis=0),
                yerr=[np.std(PRSK_wcl_norm[:,i,0],ddof=1) for i in range(len(sim.t))],
                fmt='None',ecolor='b',lw=0.05,alpha=0.1)
            plt.errorbar(sim.t,np.average(PRSK_wcl_norm[:,:,1],axis=0),
                yerr=[np.std(PRSK_wcl_norm[:,i,1],ddof=1) for i in range(len(sim.t))],
                fmt='None',ecolor='r',lw=0.05,alpha=0.1)

    e = plt.errorbar(exp.t2/60.,exp.egf_RSKw_av,yerr=exp.egf_RSKw_se,lw=1,
        markerfacecolor='None',markeredgecolor='b',fmt='bD',capsize=8,clip_on=False)
    for b in e[1]:
        b.set_clip_on(False)
    e = plt.errorbar(exp.t2/60.,exp.hrg_RSKw_av,yerr=exp.hrg_RSKw_se,lw=1,
        markerfacecolor='None',markeredgecolor='r',fmt='rs',capsize=8,clip_on=False)
    for b in e[1]:
        b.set_clip_on(False)
    plt.xlim(0,90)
    plt.xticks([0,30,60,90])
    plt.yticks([0,0.2,0.4,0.6,0.8,1,1.2])
    plt.ylim(0,1.2)
    plt.xlabel('Time (min)')
    plt.ylabel('Phosphorylated RSK\n(whole cell)')


    plt.subplot(2,4,4)
    if show_all:
        for i in range(n_file):
            plt.plot(sim.t,PCREB_wcl_all[i,:,0]/np.max(PCREB_wcl_all[i,:,:]),'b',alpha=0.05)
            plt.plot(sim.t,PCREB_wcl_all[i,:,1]/np.max(PCREB_wcl_all[i,:,:]),'r',alpha=0.05)

    if not viz_type == 'average':
        plt.plot(sim.t,sim.PCREB_wcl[:,0]/np.max(sim.PCREB_wcl[:,1]),'b')
        plt.plot(sim.t,sim.PCREB_wcl[:,1]/np.max(sim.PCREB_wcl[:,1]),'r')
    else:
        PCREB_wcl_norm  = np.empty((n_file,len(sim.tspan),sim.condition))
        for i in range(n_file):
            PCREB_wcl_norm[i,:,0] = PCREB_wcl_all[i,:,0]/np.max(PCREB_wcl_all[i,:,:])
            PCREB_wcl_norm[i,:,1] = PCREB_wcl_all[i,:,1]/np.max(PCREB_wcl_all[i,:,:])
        plt.plot(sim.t,np.average(PCREB_wcl_norm[:,:,0],axis=0),'b')
        plt.plot(sim.t,np.average(PCREB_wcl_norm[:,:,1],axis=0),'r')
        if stdev:
            plt.errorbar(sim.t,np.average(PCREB_wcl_norm[:,:,0],axis=0),
                yerr=[np.std(PCREB_wcl_norm[:,i,0],ddof=1) for i in range(len(sim.t))],
                fmt='None',ecolor='b',lw=0.05,alpha=0.1)
            plt.errorbar(sim.t,np.average(PCREB_wcl_norm[:,:,1],axis=0),
                yerr=[np.std(PCREB_wcl_norm[:,i,1],ddof=1) for i in range(len(sim.t))],
                fmt='None',ecolor='r',lw=0.05,alpha=0.1)

    e = plt.errorbar(exp.t3/60.,exp.egf_CREBw_av,yerr=exp.egf_CREBw_se,lw=1,
        markerfacecolor='None',markeredgecolor='b',fmt='bD',capsize=8,clip_on=False)
    for b in e[1]:
        b.set_clip_on(False)
    e = plt.errorbar(exp.t3/60.,exp.hrg_CREBw_av,yerr=exp.hrg_CREBw_se,lw=1,
        markerfacecolor='None',markeredgecolor='r',fmt='rs',capsize=8,clip_on=False)
    for b in e[1]:
        b.set_clip_on(False)
    plt.xlim(0,90)
    plt.xticks([0,30,60,90])
    plt.yticks([0,0.2,0.4,0.6,0.8,1,1.2])
    plt.ylim(0,1.2)
    plt.xlabel('Time (min)')
    plt.ylabel('Phosphorylated CREB\n(whole cell)')


    plt.subplot(2,4,5)
    if show_all:
        for i in range(n_file):
            plt.plot(sim.t,DUSPmRNA_all[i,:,0]/np.max(DUSPmRNA_all[i,:,:]),'b',alpha=0.05)
            plt.plot(sim.t,DUSPmRNA_all[i,:,1]/np.max(DUSPmRNA_all[i,:,:]),'r',alpha=0.05)

    if not viz_type == 'average':
        plt.plot(sim.t,sim.DUSPmRNA[:,0]/np.max(sim.DUSPmRNA[:,1]),'b')
        plt.plot(sim.t,sim.DUSPmRNA[:,1]/np.max(sim.DUSPmRNA[:,1]),'r')
    else:
        DUSPmRNA_norm  = np.empty((n_file,len(sim.tspan),sim.condition))
        for i in range(n_file):
            DUSPmRNA_norm[i,:,0] = DUSPmRNA_all[i,:,0]/np.max(DUSPmRNA_all[i,:,:])
            DUSPmRNA_norm[i,:,1] = DUSPmRNA_all[i,:,1]/np.max(DUSPmRNA_all[i,:,:])
        plt.plot(sim.t,np.average(DUSPmRNA_norm[:,:,0],axis=0),'b')
        plt.plot(sim.t,np.average(DUSPmRNA_norm[:,:,1],axis=0),'r')
        if stdev:
            plt.errorbar(sim.t,np.average(DUSPmRNA_norm[:,:,0],axis=0),
                yerr=[np.std(DUSPmRNA_norm[:,i,0],ddof=1) for i in range(len(sim.t))],
                fmt='None',ecolor='b',lw=0.05,alpha=0.1)
            plt.errorbar(sim.t,np.average(DUSPmRNA_norm[:,:,1],axis=0),
                yerr=[np.std(DUSPmRNA_norm[:,i,1],ddof=1) for i in range(len(sim.t))],
                fmt='None',ecolor='r',lw=0.05,alpha=0.1)

    e = plt.errorbar(exp.t5/60.,exp.egf_DUSPmRNA_av,yerr=exp.egf_DUSPmRNA_se,lw=1,
        markerfacecolor='None',markeredgecolor='b',fmt='bD',capsize=8,clip_on=False)
    for b in e[1]:
        b.set_clip_on(False)
    e = plt.errorbar(exp.t5/60.,exp.hrg_DUSPmRNA_av,yerr=exp.hrg_DUSPmRNA_se,lw=1,
        markerfacecolor='None',markeredgecolor='r',fmt='rs',capsize=8,clip_on=False)
    for b in e[1]:
        b.set_clip_on(False)
    plt.xlim(0,90)
    plt.xticks([0,30,60,90])
    plt.yticks([0,0.2,0.4,0.6,0.8,1,1.2])
    plt.ylim(0,1.2)
    plt.xlabel('Time (min)')
    plt.ylabel(r'$\it{dusp}$'+' mRNA\nexpression')


    plt.subplot(2,4,6)
    if show_all:
        for i in range(n_file):
            plt.plot(sim.t,cFosmRNA_all[i,:,0]/np.max(cFosmRNA_all[i,:,:]),'b',alpha=0.05)
            plt.plot(sim.t,cFosmRNA_all[i,:,1]/np.max(cFosmRNA_all[i,:,:]),'r',alpha=0.05)

    if not viz_type == 'average':
        plt.plot(sim.t,sim.cFosmRNA[:,0]/np.max(sim.cFosmRNA[:,1]),'b')
        plt.plot(sim.t,sim.cFosmRNA[:,1]/np.max(sim.cFosmRNA[:,1]),'r')
    else:
        cFosmRNA_norm  = np.empty((n_file,len(sim.tspan),sim.condition))
        for i in range(n_file):
            cFosmRNA_norm[i,:,0] = cFosmRNA_all[i,:,0]/np.max(cFosmRNA_all[i,:,:])
            cFosmRNA_norm[i,:,1] = cFosmRNA_all[i,:,1]/np.max(cFosmRNA_all[i,:,:])
        plt.plot(sim.t,np.average(cFosmRNA_norm[:,:,0],axis=0),'b')
        plt.plot(sim.t,np.average(cFosmRNA_norm[:,:,1],axis=0),'r')
        if stdev:
            plt.errorbar(sim.t,np.average(cFosmRNA_norm[:,:,0],axis=0),
                yerr=[np.std(cFosmRNA_norm[:,i,0],ddof=1) for i in range(len(sim.t))],
                fmt='None',ecolor='b',lw=0.05,alpha=0.1)
            plt.errorbar(sim.t,np.average(cFosmRNA_norm[:,:,1],axis=0),
                yerr=[np.std(cFosmRNA_norm[:,i,1],ddof=1) for i in range(len(sim.t))],
                fmt='None',ecolor='r',lw=0.05,alpha=0.1)

    e = plt.errorbar(exp.t4/60.,exp.egf_cFosmRNA_av,yerr=exp.egf_cFosmRNA_se,lw=1,
                    markerfacecolor='None',markeredgecolor='b',fmt='bD',capsize=8,clip_on=False)
    for b in e[1]:
        b.set_clip_on(False)
    e = plt.errorbar(exp.t4/60.,exp.hrg_cFosmRNA_av,yerr=exp.hrg_cFosmRNA_se,lw=1,
        markerfacecolor='None',markeredgecolor='r',fmt='rs',capsize=8,clip_on=False)
    for b in e[1]:
        b.set_clip_on(False)
    plt.xlim(0,90)
    plt.xticks([0,30,60,90])
    plt.yticks([0,0.2,0.4,0.6,0.8,1,1.2])
    plt.ylim(0,1.2)
    plt.xlabel('Time (min)')
    plt.ylabel(r'$\it{c}$'+'-'+r'$\it{fos}$'+' mRNA\nexpression')


    plt.subplot(2,4,7)
    if show_all:
        for i in range(n_file):
            plt.plot(sim.t,cFosPro_all[i,:,0]/np.max(cFosPro_all[i,:,:]),'b',alpha=0.05)
            plt.plot(sim.t,cFosPro_all[i,:,1]/np.max(cFosPro_all[i,:,:]),'r',alpha=0.05)

    if not viz_type == 'average':
        plt.plot(sim.t,sim.cFosPro[:,0]/np.max(sim.cFosPro[:,1]),'b')
        plt.plot(sim.t,sim.cFosPro[:,1]/np.max(sim.cFosPro[:,1]),'r')
    else:
        cFosPro_norm  = np.empty((n_file,len(sim.tspan),sim.condition))
        for i in range(n_file):
            cFosPro_norm[i,:,0] = cFosPro_all[i,:,0]/np.max(cFosPro_all[i,:,:])
            cFosPro_norm[i,:,1] = cFosPro_all[i,:,1]/np.max(cFosPro_all[i,:,:])
        plt.plot(sim.t,np.average(cFosPro_norm[:,:,0],axis=0),'b')
        plt.plot(sim.t,np.average(cFosPro_norm[:,:,1],axis=0),'r')
        if stdev:
            plt.errorbar(sim.t,np.average(cFosPro_norm[:,:,0],axis=0),
                yerr=[np.std(cFosPro_norm[:,i,0],ddof=1) for i in range(len(sim.t))],
                fmt='None',ecolor='b',lw=0.05,alpha=0.1)
            plt.errorbar(sim.t,np.average(cFosPro_norm[:,:,1],axis=0),
                yerr=[np.std(cFosPro_norm[:,i,1],ddof=1) for i in range(len(sim.t))],
                fmt='None',ecolor='r',lw=0.05,alpha=0.1)

    e = plt.errorbar(exp.t5/60.,exp.egf_cFosPro_av,yerr=exp.egf_cFosPro_se,lw=1,
        markerfacecolor='None',markeredgecolor='b',fmt='bD',capsize=8,clip_on=False)
    for b in e[1]:
        b.set_clip_on(False)
    e = plt.errorbar(exp.t5/60.,exp.hrg_cFosPro_av,yerr=exp.hrg_cFosPro_se,lw=1,
        markerfacecolor='None',markeredgecolor='r',fmt='rs',capsize=8,clip_on=False)
    for b in e[1]:
        b.set_clip_on(False)
    plt.xlim(0,90)
    plt.xticks([0,30,60,90])
    plt.yticks([0,0.2,0.4,0.6,0.8,1,1.2])
    plt.ylim(0,1.2)
    plt.xlabel('Time (min)')
    plt.ylabel('c-Fos Protein\nexpression')


    plt.subplot(2,4,8)
    if show_all:
        for i in range(n_file):
            plt.plot(sim.t,PcFos_all[i,:,0]/np.max(PcFos_all[i,:,:]),'b',alpha=0.05)
            plt.plot(sim.t,PcFos_all[i,:,1]/np.max(PcFos_all[i,:,:]),'r',alpha=0.05)

    if not viz_type == 'average':
        plt.plot(sim.t,sim.PcFos[:,0]/np.max(sim.PcFos[:,1]),'b')
        plt.plot(sim.t,sim.PcFos[:,1]/np.max(sim.PcFos[:,1]),'r')
    else:
        PcFos_norm  = np.empty((n_file,len(sim.tspan),sim.condition))
        for i in range(n_file):
            PcFos_norm[i,:,0] = PcFos_all[i,:,0]/np.max(PcFos_all[i,:,:])
            PcFos_norm[i,:,1] = PcFos_all[i,:,1]/np.max(PcFos_all[i,:,:])
        plt.plot(sim.t,np.average(PcFos_norm[:,:,0],axis=0),'b')
        plt.plot(sim.t,np.average(PcFos_norm[:,:,1],axis=0),'r')
        if stdev:
            plt.errorbar(sim.t,np.average(PcFos_norm[:,:,0],axis=0),
                yerr=[np.std(PcFos_norm[:,i,0],ddof=1) for i in range(len(sim.t))],
                fmt='None',ecolor='b',lw=0.05,alpha=0.1)
            plt.errorbar(sim.t,np.average(PcFos_norm[:,:,1],axis=0),
                yerr=[np.std(PcFos_norm[:,i,1],ddof=1) for i in range(len(sim.t))],
                fmt='None',ecolor='r',lw=0.05,alpha=0.1)

    e = plt.errorbar(exp.t2/60.,exp.egf_PcFos_av,yerr=exp.egf_PcFos_se,lw=1,
        markerfacecolor='None',markeredgecolor='b',fmt='bD',capsize=8,clip_on=False)
    for b in e[1]:
        b.set_clip_on(False)
    e = plt.errorbar(exp.t2/60.,exp.hrg_PcFos_av,yerr=exp.hrg_PcFos_se,lw=1,
        markerfacecolor='None',markeredgecolor='r',fmt='rs',capsize=8,clip_on=False)
    for b in e[1]:
        b.set_clip_on(False)
    plt.xlim(0,90)
    plt.xticks([0,30,60,90])
    plt.yticks([0,0.2,0.4,0.6,0.8,1,1.2])
    plt.ylim(0,1.2)
    plt.xlabel('Time (min)')
    plt.ylabel('Phosphorylated c-Fos\nProtein expression')