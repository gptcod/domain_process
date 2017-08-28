def extract_main_domain(domain):
    suffix_first = [".com", ".net", ".org", ".gov", ".mil", ".edu", ".biz", ".info", ".pro", ".name", ".coop", ".travel", ".xxx", ".idv", ".aero", ".museum", ".mobi", ".asia", ".tel", ".int", ".post", ".jobs", ".cat", ".co", ".cc", ".xyz", ".top", ".su", ".lt", ".link", ".corp", ".stream", ".site", ".email", ".online", ".win", ".ly", ".men", ".media", ".bid", ".news", ".lv", ".rs", ".space", ".sx", ".bid", ".ovh", ".gdn", ".ac", ".tech", ".dev", ".guru", ".click", ".life", ".live", ".one", ".video", ".host", ".world", ".press", ".tokyo", ".website", ".download", ".today", ".rocks", ".red"] #23
    #add co cc xyz
    suffix_second = [".ac", ".ad", ".ae", ".af", ".ag", ".ai", ".al", ".am", ".an", ".ao", ".aq", ".ar", ".as", ".at", ".au", ".aw", ".az", ".ba", ".bb", ".bd", ".be", ".bf", ".bg", ".bh", ".bi", ".bj", ".bm", ".bn", ".bo", ".br", ".bs", ".bt", ".bv", ".bw", ".by", ".bz", ".ca", ".cc", ".cd", ".cf", ".cg", ".ch", ".ci", ".ck", ".cl", ".cm", ".cn", ".co", ".cr", ".cu", ".cv", ".cx", ".cy", ".cz", ".de", ".dj", ".dk", ".dm", ".do", ".dz", ".ec", ".ee", ".eg", ".eh", ".er", ".es", ".et", ".eu", ".fi", ".fj", ".fk", ".fm", ".fo", ".fr", ".ga", ".gd", ".ge", ".gf", ".gg", ".gh", ".gi", ".gl", ".gm", ".gn", ".gp", ".gq", ".gr", ".gs", ".gt", ".gu", ".gw", ".gy", ".hk", ".hm", ".hn", ".hr", ".ht", ".hu", ".id", ".ie", ".il", ".im", ".in", ".io", ".iq", ".ir", ".is", ".it", ".je", ".jm", ".jo", ".jp", ".ke", ".kg", ".kh", ".ki", ".km", ".kn", ".kp", ".kr", ".kw", ".ky", ".kz", ".la", ".lb", ".lc", ".li", ".lk", ".lr", ".ls", ".lu", ".ma", ".mc", ".md", ".me", ".mg", ".mh", ".mk", ".ml", ".mm", ".mn", ".mo", ".mp", ".mq", ".mr", ".ms", ".mt", ".mu", ".mv", ".mw", ".mx", ".my", ".mz", ".na", ".nc", ".ne", ".nf", ".ng", ".ni", ".nl", ".no", ".np", ".nr", ".nu", ".nz", ".om", ".pa", ".pe", ".pf", ".pg", ".ph", ".pk", ".pl", ".pm", ".pn", ".pr", ".ps", ".pt", ".pw", ".py", ".qa", ".re", ".ro", ".ru", ".rw", ".sa", ".sb", ".sc", ".sd", ".se", ".sg", ".sh", ".si", ".sj", ".sk", ".sm", ".sn", ".so", ".sr", ".st", ".sv", ".sy", ".sz", ".tc", ".td", ".tf", ".tg", ".th", ".tj", ".tk", ".tl", ".tm", ".tn", ".to", ".tp", ".tr", ".tt", ".tv", ".tw", ".tz", ".ua", ".ug", ".uk", ".um", ".us", ".uy", ".uz", ".va", ".vc", ".ve", ".vg", ".vi", ".vn", ".vu", ".wf", ".ws", ".ye", ".yt", ".yu", ".yr", ".za", ".zm", ".zw", ".home", ".lan", ".club", ".local", ".intern", ".belkin"] #244
    
    whole_domain = domain
    whole_suffix = ""
    
    #print 's is ', s
    
    for s in suffix_second:
        if domain[-len(s):] == s:
            domain = domain[:len(domain) - len(s)]
            whole_suffix += s
            break
            
    for s in suffix_first:
        if domain[-len(s):] == s:
            domain = domain[:len(domain) - len(s)]
            whole_suffix += s
            break
            
    no_suffix_domain = domain
    main_strat_pos = no_suffix_domain.rfind(".")

    if main_strat_pos == -1:
         main_domain = whole_domain
    
    else:
        main_domain = whole_domain[main_strat_pos + 1:]
    
    return  main_domain