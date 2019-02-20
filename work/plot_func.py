import matplotlib.pyplot as plt

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
e = plt.errorbar(ex.t2/60.,ex.egf_MEKc_av,yerr=ex.egf_MEKc_se,lw=1,markerfacecolor='None',markeredgecolor='b',fmt='bD',capsize=8,clip_on=False)
for b in e[1]:
    b.set_clip_on(False)
e = plt.errorbar(ex.t2/60.,ex.hrg_MEKc_av,yerr=ex.hrg_MEKc_se,lw=1,markerfacecolor='None',markeredgecolor='r',fmt='rs',capsize=8,clip_on=False)
for b in e[1]:
    b.set_clip_on(False)
plt.xlim(0,90)
plt.xticks([0,30,60,90])
plt.yticks([0,0.2,0.4,0.6,0.8,1,1.2])
plt.ylim(0,1.2)
plt.xlabel('Time (min)')
plt.ylabel('Phosphorylated MEK\n(cytoplasm)')

plt.subplot(2,4,2)
plt.plot(sim.t,sim.PERK_cyt[:,0]/np.max(sim.PERK_cyt[:,1]),'b')
plt.plot(sim.t,sim.PERK_cyt[:,1]/np.max(sim.PERK_cyt[:,1]),'r')
e = plt.errorbar(ex.t2/60.,ex.egf_ERKc_av,yerr=ex.egf_ERKc_se,lw=1,markerfacecolor='None',markeredgecolor='b',fmt='bD',capsize=8,clip_on=False)
for b in e[1]:
    b.set_clip_on(False)
e = plt.errorbar(ex.t2/60.,ex.hrg_ERKc_av,yerr=ex.hrg_ERKc_se,lw=1,markerfacecolor='None',markeredgecolor='r',fmt='rs',capsize=8,clip_on=False)
for b in e[1]:
    b.set_clip_on(False)
plt.xlim(0,90)
plt.xticks([0,30,60,90])
plt.yticks([0,0.2,0.4,0.6,0.8,1,1.2])
plt.ylim(0,1.2)
plt.xlabel('Time (min)')
plt.ylabel('Phosphorylated ERK\n(cytoplasm)')

plt.subplot(2,4,3)
plt.plot(sim.t,sim.PRSK_wcl[:,0]/np.max(sim.PRSK_wcl[:,1]),'b')
plt.plot(sim.t,sim.PRSK_wcl[:,1]/np.max(sim.PRSK_wcl[:,1]),'r')
e = plt.errorbar(ex.t2/60.,ex.egf_RSKw_av,yerr=ex.egf_RSKw_se,lw=1,markerfacecolor='None',markeredgecolor='b',fmt='bD',capsize=8,clip_on=False)
for b in e[1]:
    b.set_clip_on(False)
e = plt.errorbar(ex.t2/60.,ex.hrg_RSKw_av,yerr=ex.hrg_RSKw_se,lw=1,markerfacecolor='None',markeredgecolor='r',fmt='rs',capsize=8,clip_on=False)
for b in e[1]:
    b.set_clip_on(False)
plt.xlim(0,90)
plt.xticks([0,30,60,90])
plt.yticks([0,0.2,0.4,0.6,0.8,1,1.2])
plt.ylim(0,1.2)
plt.xlabel('Time (min)')
plt.ylabel('Phosphorylated RSK\n(whole cell)')

plt.subplot(2,4,4)
plt.plot(sim.t,sim.PCREB_wcl[:,0]/np.max(sim.PCREB_wcl[:,1]),'b')
plt.plot(sim.t,sim.PCREB_wcl[:,1]/np.max(sim.PCREB_wcl[:,1]),'r')
e = plt.errorbar(ex.t3/60.,ex.egf_CREBw_av,yerr=ex.egf_CREBw_se,lw=1,markerfacecolor='None',markeredgecolor='b',fmt='bD',capsize=8,clip_on=False)
for b in e[1]:
    b.set_clip_on(False)
e = plt.errorbar(ex.t3/60.,ex.hrg_CREBw_av,yerr=ex.hrg_CREBw_se,lw=1,markerfacecolor='None',markeredgecolor='r',fmt='rs',capsize=8,clip_on=False)
for b in e[1]:
    b.set_clip_on(False)
plt.xlim(0,90)
plt.xticks([0,30,60,90])
plt.yticks([0,0.2,0.4,0.6,0.8,1,1.2])
plt.ylim(0,1.2)
plt.xlabel('Time (min)')
plt.ylabel('Phosphorylated CREB\n(whole cell)')

plt.subplot(2,4,5)
plt.plot(sim.t,sim.DUSPmRNA[:,0]/np.max(sim.DUSPmRNA[:,1]),'b')
plt.plot(sim.t,sim.DUSPmRNA[:,1]/np.max(sim.DUSPmRNA[:,1]),'r')
e = plt.errorbar(ex.t5/60.,ex.egf_DUSPmRNA_av,yerr=ex.egf_DUSPmRNA_se,lw=1,markerfacecolor='None',markeredgecolor='b',fmt='bD',capsize=8,clip_on=False)
for b in e[1]:
    b.set_clip_on(False)
e = plt.errorbar(ex.t5/60.,ex.hrg_DUSPmRNA_av,yerr=ex.hrg_DUSPmRNA_se,lw=1,markerfacecolor='None',markeredgecolor='r',fmt='rs',capsize=8,clip_on=False)
for b in e[1]:
    b.set_clip_on(False)
plt.xlim(0,90)
plt.xticks([0,30,60,90])
plt.yticks([0,0.2,0.4,0.6,0.8,1,1.2])
plt.ylim(0,1.2)
plt.xlabel('Time (min)')
plt.ylabel(r'$\it{dusp}$'+' mRNA\nexpression')

plt.subplot(2,4,6)
plt.plot(sim.t,sim.cFosmRNA[:,0]/np.max(sim.cFosmRNA[:,1]),'b')
plt.plot(sim.t,sim.cFosmRNA[:,1]/np.max(sim.cFosmRNA[:,1]),'r')
e = plt.errorbar(ex.t4/60.,ex.egf_cFosmRNA_av,yerr=ex.egf_cFosmRNA_se,lw=1,markerfacecolor='None',markeredgecolor='b',fmt='bD',capsize=8,clip_on=False)
for b in e[1]:
    b.set_clip_on(False)
e = plt.errorbar(ex.t4/60.,ex.hrg_cFosmRNA_av,yerr=ex.hrg_cFosmRNA_se,lw=1,markerfacecolor='None',markeredgecolor='r',fmt='rs',capsize=8,clip_on=False)
for b in e[1]:
    b.set_clip_on(False)
plt.xlim(0,90)
plt.xticks([0,30,60,90])
plt.yticks([0,0.2,0.4,0.6,0.8,1,1.2])
plt.ylim(0,1.2)
plt.xlabel('Time (min)')
plt.ylabel(r'$\it{c}$'+'-'+r'$\it{fos}$'+' mRNA\nexpression')

plt.subplot(2,4,7)
plt.plot(sim.t,sim.cFosPro[:,0]/np.max(sim.cFosPro[:,1]),'b')
plt.plot(sim.t,sim.cFosPro[:,1]/np.max(sim.cFosPro[:,1]),'r')
e = plt.errorbar(ex.t5/60.,ex.egf_cFosPro_av,yerr=ex.egf_cFosPro_se,lw=1,markerfacecolor='None',markeredgecolor='b',fmt='bD',capsize=8,clip_on=False)
for b in e[1]:
    b.set_clip_on(False)
e = plt.errorbar(ex.t5/60.,ex.hrg_cFosPro_av,yerr=ex.hrg_cFosPro_se,lw=1,markerfacecolor='None',markeredgecolor='r',fmt='rs',capsize=8,clip_on=False)
for b in e[1]:
    b.set_clip_on(False)
plt.xlim(0,90)
plt.xticks([0,30,60,90])
plt.yticks([0,0.2,0.4,0.6,0.8,1,1.2])
plt.ylim(0,1.2)
plt.xlabel('Time (min)')
plt.ylabel('c-Fos Protein\nexpression')

plt.subplot(2,4,8)
plt.plot(sim.t,sim.PcFos[:,0]/np.max(sim.PcFos[:,1]),'b')
plt.plot(sim.t,sim.PcFos[:,1]/np.max(sim.PcFos[:,1]),'r')
e = plt.errorbar(ex.t2/60.,ex.egf_PcFos_av,yerr=ex.egf_PcFos_se,lw=1,markerfacecolor='None',markeredgecolor='b',fmt='bD',capsize=8,clip_on=False)
for b in e[1]:
    b.set_clip_on(False)
e = plt.errorbar(ex.t2/60.,ex.hrg_PcFos_av,yerr=ex.hrg_PcFos_se,lw=1,markerfacecolor='None',markeredgecolor='r',fmt='rs',capsize=8,clip_on=False)
for b in e[1]:
    b.set_clip_on(False)
plt.xlim(0,90)
plt.xticks([0,30,60,90])
plt.yticks([0,0.2,0.4,0.6,0.8,1,1.2])
plt.ylim(0,1.2)
plt.xlabel('Time (min)')
plt.ylabel('Phosphorylated c-Fos\nProtein expression')