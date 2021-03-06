# Shamelessly borrowed from oyoyo, who borrowed it from irclib,
# who mostly got it from Net::IRC, and so on...
NUMERIC_EVENTS = {
    "001": "WELCOME",
    "002": "YOURHOST",
    "003": "CREATED",
    "004": "MYINFO",
    "005": "FEATURELIST",
    "200": "TRACELINK",
    "201": "TRACECONNECTING",
    "202": "TRACEHANDSHAKE",
    "203": "TRACEUNKNOWN",
    "204": "TRACEOPERATOR",
    "205": "TRACEUSER",
    "206": "TRACESERVER",
    "207": "TRACESERVICE",
    "208": "TRACENEWTYPE",
    "209": "TRACECLASS",
    "210": "TRACERECONNECT",
    "211": "STATSLINKINFO",
    "212": "STATSCOMMANDS",
    "213": "STATSCLINE",
    "214": "STATSNLINE",
    "215": "STATSILINE",
    "216": "STATSKLINE",
    "217": "STATSQLINE",
    "218": "STATSYLINE",
    "219": "ENDOFSTATS",
    "221": "UMODEIS",
    "231": "SERVICEINFO",
    "232": "ENDOFSERVICES",
    "233": "SERVICE",
    "234": "SERVLIST",
    "235": "SERVLISTEND",
    "241": "STATSLLINE",
    "242": "STATSUPTIME",
    "243": "STATSOLINE",
    "244": "STATSHLINE",
    "250": "LUSERCONNS",
    "251": "LUSERCLIENT",
    "252": "LUSEROP",
    "253": "LUSERUNKNOWN",
    "254": "LUSERCHANNELS",
    "255": "LUSERME",
    "256": "ADMINME",
    "257": "ADMINLOC1",
    "258": "ADMINLOC2",
    "259": "ADMINEMAIL",
    "261": "TRACELOG",
    "262": "ENDOFTRACE",
    "263": "TRYAGAIN",
    "265": "N_LOCAL",
    "266": "N_GLOBAL",
    "300": "NONE",
    "301": "AWAY",
    "302": "USERHOST",
    "303": "ISON",
    "305": "UNAWAY",
    "306": "NOWAWAY",
    "307": "WHOISREGNICK", # Aaeriele 2013-06-16
    "311": "WHOISUSER",
    "312": "WHOISSERVER",
    "313": "WHOISOPERATOR",
    "314": "WHOWASUSER",
    "315": "ENDOFWHO",
    "316": "WHOISCHANOP",
    "317": "WHOISIDLE",
    "318": "ENDOFWHOIS",
    "319": "WHOISCHANNELS",
    "321": "LISTSTART",
    "322": "LIST",
    "323": "LISTEND",
    "324": "CHANNELMODEIS",
    "329": "CHANNELCREATE",
    "330": "WHOISACCOUNT", # Aaeriele 2013-06-16
    "331": "NOTOPIC",
    "332": "CURRENTTOPIC",
    "333": "TOPICINFO",
    "335": "WHOISBOT", # Aaeriele 2013-06-16
    "341": "INVITING",
    "342": "SUMMONING",
    "346": "INVITELIST",
    "347": "ENDOFINVITELIST",
    "348": "EXCEPTLIST",
    "349": "ENDOFEXCEPTLIST",
    "351": "VERSION",
    "352": "WHOREPLY",
    "353": "NAMREPLY",
    "361": "KILLDONE",
    "362": "CLOSING",
    "363": "CLOSEEND",
    "364": "LINKS",
    "365": "ENDOFLINKS",
    "366": "ENDOFNAMES",
    "367": "BANLIST",
    "368": "ENDOFBANLIST",
    "369": "ENDOFWHOWAS",
    "371": "INFO",
    "372": "MOTD",
    "373": "INFOSTART",
    "374": "ENDOFINFO",
    "375": "MOTDSTART",
    "376": "ENDOFMOTD",
    "377": "MOTD2",        # 1997-10-16 -- TKIL
    "381": "YOUREOPER",
    "382": "REHASHING",
    "384": "MYPORTIS",
    "391": "TIME",
    "392": "USERSSTART",
    "393": "USERS",
    "394": "ENDOFUSERS",
    "395": "NOUSERS",
    "401": "NOSUCHNICK",
    "402": "NOSUCHSERVER",
    "403": "NOSUCHCHANNEL",
    "404": "CANNOTSENDTOCHAN",
    "405": "TOOMANYCHANNELS",
    "406": "WASNOSUCHNICK",
    "407": "TOOMANYTARGETS",
    "409": "NOORIGIN",
    "411": "NORECIPIENT",
    "412": "NOTEXTTOSEND",
    "413": "NOTOPLEVEL",
    "414": "WILDTOPLEVEL",
    "421": "UNKNOWNCOMMAND",
    "422": "NOMOTD",
    "423": "NOADMININFO",
    "424": "FILEERROR",
    "431": "NONICKNAMEGIVEN",
    "432": "ERRONEUSNICKNAME", # THISS IZ HOW ITS SPELD IN THEE RFC.
    "433": "NICKNAMEINUSE",
    "436": "NICKCOLLISION",
    "437": "UNAVAILRESOURCE",  # "NICK TEMPORALLY UNAVAILABLE"
    "441": "USERNOTINCHANNEL",
    "442": "NOTONCHANNEL",
    "443": "USERONCHANNEL",
    "444": "NOLOGIN",
    "445": "SUMMONDISABLED",
    "446": "USERSDISABLED",
    "451": "NOTREGISTERED",
    "461": "NEEDMOREPARAMS",
    "462": "ALREADYREGISTERED",
    "463": "NOPERMFORHOST",
    "464": "PASSWDMISMATCH",
    "465": "YOUREBANNEDCREEP", # I LOVE THIS ONE...
    "466": "YOUWILLBEBANNED",
    "467": "KEYSET",
    "471": "CHANNELISFULL",
    "472": "UNKNOWNMODE",
    "473": "INVITEONLYCHAN",
    "474": "BANNEDFROMCHAN",
    "475": "BADCHANNELKEY",
    "476": "BADCHANMASK",
    "477": "NOCHANMODES",  # "CHANNEL DOESN'T SUPPORT MODES"
    "478": "BANLISTFULL",
    "481": "NOPRIVILEGES",
    "482": "CHANOPRIVSNEEDED",
    "483": "CANTKILLSERVER",
    "484": "RESTRICTED",   # CONNECTION IS RESTRICTED
    "485": "UNIQOPPRIVSNEEDED",
    "491": "NOOPERHOST",
    "492": "NOSERVICEHOST",
    "501": "UMODEUNKNOWNFLAG",
    "502": "USERSDONTMATCH",
}

# vim: set ts=4 sts=4 sw=4 et:
