from scipy.spatial.distance import cosine

def compute_objval_abs(sim_data,exp_data):  # Residual Sum of Squares

    return np.dot((sim_data-exp_data),(sim_data-exp_data))


def compute_objval_cs(sim_data,exp_data):  # Cosine similarity

    return cosine(sim_data,exp_data)


def get_fitness(individual_gene,search_idx,search_region):

    (x,y0) = update_param(individual_gene,search_idx,search_region)
    # constraints
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

    exp = ExperimentalData()
    sim = Simulation(x,y0)

    if sim.run_simulation(x,y0) is None:
      fit=np.zeros(7)

      # ERK
      norm_max = np.max(sim.PERK_cyt)
      fit[0] = compute_objval_abs(
          np.r_[sim.PERK_cyt[exp.t2,0],sim.PERK_cyt[exp.t2,1]]/norm_max,
          np.r_[exp.egf_ERKc_av,exp.hrg_ERKc_av]
      )
      # RSK
      norm_max = np.max(sim.PRSK_wcl)
      fit[1] = compute_objval_abs(
          np.r_[sim.PRSK_wcl[exp.t2,0],sim.PRSK_wcl[exp.t2,1]]/norm_max,
          np.r_[exp.egf_RSKw_av,exp.hrg_RSKw_av]
      )
      # CREB
      norm_max = np.max(sim.PCREB_wcl)
      fit[2] = compute_objval_abs(
          np.r_[sim.PCREB_wcl[exp.t3,0],sim.PCREB_wcl[exp.t3,1]]/norm_max,
          np.r_[exp.egf_CREBw_av,exp.hrg_CREBw_av]
      )
      # DUSPmRNA
      norm_max = np.max(sim.DUSPmRNA)
      fit[3] = compute_objval_abs(
          np.r_[sim.DUSPmRNA[exp.t5,0],sim.DUSPmRNA[exp.t5,1]]/norm_max,
          np.r_[exp.egf_DUSPmRNA_av,exp.hrg_DUSPmRNA_av]
      )
      # cFosmRNA
      norm_max = np.max(sim.cFosmRNA)
      fit[4] = compute_objval_abs(
          np.r_[sim.cFosmRNA[exp.t4,0],sim.cFosmRNA[exp.t4,1]]/norm_max,
          np.r_[exp.egf_cFosmRNA_av,exp.hrg_cFosmRNA_av]
      )
      # cFosPro
      norm_max = np.max(sim.cFosPro)
      fit[5] = compute_objval_abs(
          np.r_[sim.cFosPro[exp.t5,0],sim.cFosPro[exp.t5,1]]/norm_max,
          np.r_[exp.egf_cFosPro_av,exp.hrg_cFosPro_av]
      )
      # PcFos
      norm_max = np.max(sim.PcFos)
      fit[6] = compute_objval_abs(
          np.r_[sim.PcFos[exp.t2,0],sim.PcFos[exp.t2,1]]/norm_max,
          np.r_[exp.egf_PcFos_av,exp.hrg_PcFos_av]
      )

      return np.sum(fit)

    else:

      return np.inf