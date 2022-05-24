from dataclasses import dataclass


@dataclass
class OldDamageConfig:
  PART_ADJACENCY_GRAPH = {'Back Bumper': ['Left Qtr Panel',
  'Right Qtr Panel',
  'Tail Gate',
  'Left Taillight',
  'Right Taillight',
  'Rear Reflector Top',
  'Rear Reflector Bottom',
  'Back Bumper Cover',
  'Rear PDC Sensor',
  'License Plate',
  'Left Qtr Extender',
  'Right Qtr Extender'],
  'Back Bumper Cover': ['Back Bumper'],
  'Back Glass': ['Left Pillar C',
  'Right Pillar C',
  'Tail Gate',
  'Roof',
  'Left Qtr Panel',
  'Right Qtr Panel'],
  'Bumper Grill Bottom': ['Bumper Grill Top', 'Front Bumper'],
  'Bumper Grill Top': ['Bumper Grill Bottom', 'Front Bumper'],
  'Carrier': ['Roof'],
  'Front Bumper': ['Hood',
  'Left Fender',
  'Right Fender',
  'Left Headlight',
  'Right Headlight',
  'Bumper Grill Top',
  'Bumper Grill Bottom',
  'Front Bumper Cover',
  'Front PDC Sensor',
  'Left Fog Light',
  'Right Fog Light',
  'Left Fender Extender',
  'Right Fender Extender'],
  'Front Bumper Cover': ['Front Bumper'],
  'Front Glass': ['Hood', 'Left Pillar A', 'Right Pillar A', 'Roof'],
  'Front PDC Sensor': ['Front Bumper'],
  'Fuel Door': ['Left Qtr Panel'],
  'Hood': ['Front Glass',
  'Front Bumper',
  'Left Fender',
  'Right Fender',
  'Left Headlight',
  'Right Headlight'],
  'Left Door Moulding': ['Left Front Door', 'Left Rear Door'],
  'Left Fender': ['Left Front Door',
  'Front Bumper',
  'Hood',
  'Left Pillar A',
  'Left Headlight',
  'Left Side View Mirror',
  'Left Fender Extender',
  'Left Front Wheel Rim'],
  'Left Fender Extender': ['Left Fender',
  'Front Bumper',
  'Left Front Wheel Rim'],
  'Left Fog Light': ['Front Bumper'],
  'Left Front Door': ['Left Rear Door',
  'Left Front Window Glass',
  'Left Fender',
  'Left Running Board',
  'Left Pillar A',
  'Left Pillar B',
  'Left Side View Mirror',
  'Left Front Door Handle',
  'Left Door Moulding',
  'Left Stair'],
  'Left Front Door Handle': ['Left Front Door'],
  'Left Front Wheel Rim': ['Left Fender', 'Left Fender Extender'],
  'Left Front Window Glass': ['Left Pillar A',
  'Left Pillar B',
  'Left Front Door',
  'Left Side View Mirror',
  'Roof'],
  'Left Headlight': ['Front Bumper', 'Left Fender', 'Hood'],
  'Left Pillar A': ['Left Front Window Glass',
  'Front Glass',
  'Left Fender',
  'Left Front Door',
  'Roof'],
  'Left Pillar B': ['Left Rear Window Glass',
  'Left Front Window Glass',
  'Left Front Door',
  'Left Rear Door',
  'Roof'],
  'Left Pillar C': ['Left Rear Window Glass',
  'Left Qtr Window Glass',
  'Back Glass',
  'Left Qtr Panel',
  'Roof'],
  'Left Qtr Extender': ['Left Qtr Panel',
  'Back Bumper',
  'Left Rear Door',
  'Left Rear Wheel Rim'],
  'Left Qtr Panel': ['Left Rear Door',
  'Left Taillight',
  'Left Pillar C',
  'Left Running Board',
  'Tail Gate',
  'Back Bumper',
  'Left Qtr Extender',
  'Back Glass',
  'Fuel Door',
  'Left Rear Wheel Rim'],
  'Left Qtr Window Glass': ['Left Qtr Panel', 'Left Pillar C'],
  'Left Rear Door': ['Left Front Door',
  'Left Rear Window Glass',
  'Left Qtr Panel',
  'Left Running Board',
  'Left Pillar B',
  'Left Pillar C',
  'Left Rear Door Handle',
  'Left Door Moulding',
  'Left Qtr Extender',
  'Left Stair'],
  'Left Rear Door Handle': ['Left Rear Door'],
  'Left Rear Wheel Rim': ['Left Qtr Panel', 'Left Qtr Extender'],
  'Left Rear Window Glass': ['Left Pillar B',
  'Left Pillar C',
  'Left Rear Door',
  'Roof'],
  'Left Running Board': ['Left Fender',
  'Left Front Door',
  'Left Rear Door',
  'Left Qtr Panel',
  'Left Stair'],
  'Left Side View Mirror': ['Left Pillar A',
  'Left Front Window Glass',
  'Left Front Door',
  'Left Fender'],
  'Left Stair': ['Left Running Board', 'Left Front Door', 'Left Rear Door'],
  'Left Taillight': ['Left Qtr Panel', 'Tail Gate', 'Back Bumper'],
  'Left Wheel': [],
  'License Plate': ['Back Bumper'],
  'Rear PDC Sensor': ['Back Bumper'],
  'Rear Reflector Bottom': ['Back Bumper'],
  'Rear Reflector Top': ['Back Bumper'],
  'Right Door Moulding': ['Right Front Door', 'Right Rear Door'],
  'Right Fender': ['Right Front Door',
  'Front Bumper',
  'Hood',
  'Right Pillar A',
  'Right Headlight',
  'Right Side View Mirror',
  'Right Fender Extender',
  'Right Front Wheel Rim'],
  'Right Fender Extender': ['Right Fender',
  'Front Bumper',
  'Right Front Wheel Rim'],
  'Right Fog Light': ['Front Bumper'],
  'Right Front Door': ['Right Rear Door',
  'Right Front Window Glass',
  'Right Fender',
  'Right Running Board',
  'Right Pillar A',
  'Right Pillar B',
  'Right Side View Mirror',
  'Right Front Door Handle',
  'Right Door Moulding',
  'Right Stair'],
  'Right Front Door Handle': ['Right Front Door'],
  'Right Front Wheel Rim': ['Right Fender', 'Right Fender Extender'],
  'Right Front Window Glass': ['Right Pillar A',
  'Right Pillar B',
  'Right Front Door',
  'Right Side View Mirror',
  'Roof'],
  'Right Headlight': ['Front Bumper', 'Right Fender', 'Hood'],
  'Right Pillar A': ['Right Front Window Glass',
  'Front Glass',
  'Right Fender',
  'Right Front Door',
  'Roof'],
  'Right Pillar B': ['Right Rear Window Glass',
  'Right Front Window Glass',
  'Right Front Door',
  'Right Rear Door',
  'Roof'],
  'Right Pillar C': ['Right Rear Window Glass',
  'Right Qtr Window Glass',
  'Back Glass',
  'Right Qtr Panel',
  'Roof'],
  'Right Qtr Extender': ['Right Qtr Panel',
  'Back Bumper',
  'Right Rear Door',
  'Right Rear Wheel Rim'],
  'Right Qtr Panel': ['Right Rear Door',
  'Right Taillight',
  'Right Pillar C',
  'Right Running Board',
  'Tail Gate',
  'Back Bumper',
  'Right Qtr Extender',
  'Back Glass',
  'Right Rear Wheel Rim'],
  'Right Qtr Window Glass': ['Right Qtr Panel', 'Right Pillar C'],
  'Right Rear Door': ['Right Front Door',
  'Right Rear Window Glass',
  'Right Qtr Panel',
  'Right Running Board',
  'Right Pillar B',
  'Right Pillar C',
  'Right Rear Door Handle',
  'Right Door Moulding',
  'Right Qtr Extender',
  'Right Stair'],
  'Right Rear Door Handle': ['Right Rear Door'],
  'Right Rear Wheel Rim': ['Right Qtr Panel', 'Right Qtr Extender'],
  'Right Rear Window Glass': ['Right Pillar B',
  'Right Pillar C',
  'Right Rear Door',
  'Roof'],
  'Right Running Board': ['Right Fender',
  'Right Front Door',
  'Right Rear Door',
  'Right Qtr Panel',
  'Right Stair'],
  'Right Side View Mirror': ['Right Pillar A',
  'Right Front Window Glass',
  'Right Front Door',
  'Right Fender'],
  'Right Stair': ['Right Running Board', 'Right Front Door', 'Right Rear Door'],
  'Right Taillight': ['Right Qtr Panel', 'Tail Gate', 'Back Bumper'],
  'Right Wheel': [],
  'Roof': ['Front Glass',
  'Back Glass',
  'Left Front Window Glass',
  'Left Rear Window Glass',
  'Right Front Window Glass',
  'Right Rear Window Glass',
  'Left Pillar A',
  'Left Pillar B',
  'Left Pillar C',
  'Right Pillar A',
  'Right Pillar B',
  'Right Pillar C',
  'Carrier'],
  'Spoiler': ['Tail Gate'],
  'Stepney': [],
  'Tail Gate': ['Left Taillight',
  'Right Taillight',
  'Back Bumper',
  'Back Glass',
  'Left Qtr Panel',
  'Right Qtr Panel',
  'Left Pillar C',
  'Right Pillar C',
  'Spoiler']
  }


  PARTS_LIST_OF_SPECIFIC_SIDE = {'Front': [ 'Front Bumper',
                                          'Left Headlight',
                                          'Right Headlight',
                                          'Hood',
                                          'Front Glass',
                                          'Bumper Grill Top',
                                          'Bumper Grill Bottom',
                                          'Left Fog Light',
                                          'Right Fog Light',
                                          'Front Bumper Cover',
                                          'Front PDC Sensor'
                                        ],
                               
                                'Left': [ 'Left Fender',
                                          'Left Side View Mirror',
                                          'Left Front Door',
                                          'Left Rear Door',
                                          'Left Running Board',
                                          'Left Front Window Glass',
                                          'Left Rear Window Glass',
                                          'Left Qtr Window Glass',
                                          'Left Door Moulding',
                                          'Left Pillar A',
                                          'Left Pillar B',
                                          'Left Pillar C',
                                          'Left Qtr Panel',
                                          'Fuel Door',
                                          'Left Stair',
                                          'Left Wheel',
                                          'Left Front Wheel Rim',
                                          'Left Rear Wheel Rim',
                                          'Left Fender Extender',
                                          'Left Qtr Extender',
                                          'Left Front Door Handle',
                                          'Left Rear Door Handle'
                                        ],
                               
                                'Rear': [ 'Back Glass',
                                          'Tail Gate',
                                          'Left Taillight',
                                          'Right Taillight',
                                          'Back Bumper',
                                          'Rear Reflector Top',
                                          'Rear Reflector Bottom',
                                          'Spoiler',
                                          'License Plate',
                                          'Stepney',
                                          'Back Bumper Cover',
                                          'Rear PDC Sensor'
                                        ],
                               
                              'Right' : [ 'Right Fender',
                                          'Right Side View Mirror',
                                          'Right Front Door',
                                          'Right Rear Door',
                                          'Right Running Board',
                                          'Right Front Window Glass',
                                          'Right Rear Window Glass',
                                          'Right Qtr Window Glass',
                                          'Right Door Moulding',
                                          'Right Pillar A',
                                          'Right Pillar B',
                                          'Right Pillar C',
                                          'Right Qtr Panel',
                                          'Right Stair',
                                          'Right Wheel',
                                          'Right Front Wheel Rim',
                                          'Right Rear Wheel Rim',
                                          'Right Fender Extender',
                                          'Right Qtr Extender',
                                          'Right Front Door Handle',
                                          'Right Rear Door Handle'
                                          ],
                               
                                'Top' : [ 'Roof',
                                         'Carrier'
                                        ] }


  NON_STANDALONE_DAMAGES = [ 'Bumper Grill Top',
                            'Bumper Grill Bottom',
                            'Left Fog Light',
                            'Right Fog Light',
                            'Rear Reflector Bottom',
                            'Rear Reflector Top'
                          ]

  # category wise classification of damages
  CATEGORY_4_DAMAGES = ['deep_dent', 'broken', 'tear', 'tear_major', 'shatter_major', 'dislocation_major', 
                        'dislocation', 'stitch', 'collision_damage', 'line_dent_major', 'hole',
                        'spider_core', 'spread', 'dislocation_2', 'dislocation_2_major', 'shatter', 'crack']

  CATEGORY_3_DAMAGES = ['shallow_dent_major', 'design_dent_major', 'edge_dent', 'shatter_minor', 'tear_minor', 'line_dent_minor',  
                        'shallow_dent', 'design_dent', 'shallow_dent_minor', 'design_dent_minor']

  CATEGORY_2_DAMAGES = ['chip_off', 'scratch_major']

  CATEGORY_1_DAMAGES = ['scratch_minor', 'spot', 'scratch_or_spot', 'dislocation_minor', 
                        'screw', 'stitch_or_screw', 'dislocation_2_minor']

  RUST={'rust', 'rust_internal', 'rust_external','AI uncertain'}

  AI_UNCERTAIN={'AI uncertain'}
