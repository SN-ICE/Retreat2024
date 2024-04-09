sn_lines = {
    'Ca II H&K': {'rest': 3945.12,
                  'lo_range': (3500., 3800.),
                  'hi_range': (3900., 4100.)},
    'Si II 4000A': {'rest': 4129.73,
                    'lo_range': (3900., 4000.),
                    'hi_range': (4000., 4150.)},
    'Mg II 4300A': {'rest': 4481.2,
                    'lo_range': (3900., 4150.),
                    'hi_range': (4450., 4700.)},
    # 'Si III 4450A': {'rest': 4481.2,
    #                 'lo_range': (4300., 4420.),
    #                 'hi_range': (4500., 4600.)},
    'Fe II 4800A': {'rest': 5083.42,
                    'lo_range': (4500., 4700.),
                    'hi_range': (5050., 5550.)},
    'S II 5500A': {'rest': 5536.24,
                   'lo_range': (5150., 5300.),
                   'hi_range': (5500., 5700.)},
    'Si II 5800A': {'rest': 5972.0,
                    'lo_range': (5550., 5700.),
                    'hi_range': (5800., 6000.)},
    'Si II 6150A': {'rest': 6355.0,
                    'lo_range': (5800., 6000.),
                    'hi_range': (6200., 6600.)},
            #        'lo_range_hv': (5700., 6000.),
            #        'hi_range_hv': (6150., 6400.)},
    'O I 7500A': {'rest': 7773.,
                  'lo_range': (7250., 7350.),
                  'hi_range': (7500., 7750.)},
     'Ca II 8542A': {'rest': 8542.,
                  'lo_range': (7500., 8000.),
                  'hi_range': (8200., 8900.)},            
    'Fe II': {'rest': 5169.,
              'lo_range': (4950., 5050.),
              'hi_range': (5150., 5250.)},
    'He I': {'rest': 5875.,
             'lo_range': (5350., 5450.),
             'hi_range': (5850., 6000.)},
    'H alpha': {'rest': 6350.,
             'lo_range': (6200., 6300.),
             'hi_range': (6450., 6550.)},
    'H beta': {'rest': 4690.,
             'lo_range': (4520., 4620.),
             'hi_range': (4700., 4800.)}           
}

sn_types = {
    'Ia': (
        'Ca II H&K',
        'Si II 4000A',
        'Mg II 4300A',
        # 'Si III 4450A',
        'Fe II 4800A',
        'S II 5500A',
        'Si II 5800A',
        'Si II 6150A',
        'O I 7500A',
        'Ca II 8542A',
    ),
    'Ib': (
        'Fe II',
        'He I'
    ),
    'Ic': (
        'Fe II',
        'O I 7500A'
    ),
        'II': (   #Type II & IIb
        'He I',
        'H alpha',
        'H beta'
    )
}


def get_features(sn_type: str):
    lines = sn_types[sn_type]

    line_info = {}
    for line in lines:
        line_info[line] = sn_lines[line]

    return line_info
