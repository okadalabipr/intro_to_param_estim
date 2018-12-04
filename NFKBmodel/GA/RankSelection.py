def RankSelection(n_family):
    ranking = np.repeat(np.arange(1,n_family),np.arange(1,n_family)[-1::-1])

    np.random.shuffle(ranking)

    idx = np.random.randint(len(ranking))
    ic1 = ranking[idx]

    return ic1
