from scipy.spatial.distance import cosine

def compute_objval_abs(sim_data,ex_data):  # Residual Sum of Squares

    return np.dot((sim_data-ex_data),(sim_data-ex_data))


def compute_objval_cs(sim_data,ex_data):  # Cosine similarity

    return cosine(sim_data,ex_data)


def get_fitness(individual_gene,search_idx,search_region):

    (x,y0) = update_param(individual_gene,search_idx,search_region)
    #constraints
    x[V6] = x[V5]
    x[Km6] = x[Km5]
    x[KimpDUSP] = x[KimDUSP]
    x[KexpDUSP] = x[KexDUSP]
    x[KimpcFOS] = x[KimFOS]
    x[KexpcFOS] = x[KexFOS]
    x[p52] = x[p47]
    x[m52] = x[m47]
    x[p53] = x[p48]
    x[p54] = x[p49]
    x[m54] = x[m49]
    x[p55] = x[p50]
    x[p56] = x[p51]
    x[m56] = x[m51]

    ex = ExperimentalData()
    sim = Simulation(x,y0)

    if sim.run_simulation(x,y0) == False:
      return np.inf
    else:
      fit=np.zeros(7)

      #ERK
      norm_max = np.max(sim.PERK_cyt)
      fit[0] = compute_objval_abs(np.append(sim.PERK_cyt[ex.t2,0],sim.PERK_cyt[ex.t2,1])/norm_max,np.append(ex.egf_ERKc_av,ex.hrg_ERKc_av))
      #RSK
      norm_max = np.max(sim.PRSK_wcl)
      fit[1] = compute_objval_abs(np.append(sim.PRSK_wcl[ex.t2,0],sim.PRSK_wcl[ex.t2,1])/norm_max,np.append(ex.egf_RSKw_av,ex.hrg_RSKw_av))
      #CREB
      norm_max = np.max(sim.PCREB_wcl)
      fit[2] = compute_objval_abs(np.append(sim.PCREB_wcl[ex.t3,0],sim.PCREB_wcl[ex.t3,1])/norm_max,np.append(ex.egf_CREBw_av,ex.hrg_CREBw_av))
      #DUSPmRNA
      norm_max = np.max(sim.DUSPmRNA)
      fit[3] = compute_objval_abs(np.append(sim.DUSPmRNA[ex.t5,0],sim.DUSPmRNA[ex.t5,1])/norm_max,np.append(ex.egf_DUSPmRNA_av,ex.hrg_DUSPmRNA_av))
      #cFosmRNA
      norm_max = np.max(sim.cFosmRNA)
      fit[4] = compute_objval_abs(np.append(sim.cFosmRNA[ex.t4,0],sim.cFosmRNA[ex.t4,1])/norm_max,np.append(ex.egf_cFosmRNA_av,ex.hrg_cFosmRNA_av))
      #cFosPro
      norm_max = np.max(sim.cFosPro)
      fit[5] = compute_objval_abs(np.append(sim.cFosPro[ex.t5,0],sim.cFosPro[ex.t5,1])/norm_max,np.append(ex.egf_cFosPro_av,ex.hrg_cFosPro_av))
      #PcFos
      norm_max = np.max(sim.PcFos)
      fit[6] = compute_objval_abs(np.append(sim.PcFos[ex.t2,0],sim.PcFos[ex.t2,1])/norm_max,np.append(ex.egf_PcFos_av,ex.hrg_PcFos_av))

      return np.sum(fit)