APRICOT_MODELS = [
    {
        "classifier": "resnet50",
        "id": 0,
        "model": "frcnn",
        "url": "http://download.tensorflow.org/models/object_detection/faster_rcnn_resnet50_coco_2018_01_28.tar.gz",
    },
    {
        "classifier": "resnet50",
        "id": 1,
        "model": "retinanet",
        "url": "http://download.tensorflow.org/models/object_detection/ssd_resnet50_v1_fpn_shared_box_predictor_640x640_coco14_sync_2018_07_03.tar.gz",
    },
    {
        "classifier": "mobilenetv1",
        "id": 2,
        "model": "ssd",
        "url": "http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v1_coco_2018_01_28.tar.gz",
    },
]

APRICOT_PATCHES = {
    0: {
        "adv_model": 0,
        "adv_target": 53,
        "id": 0,
        "is_circle": True,
        "is_square": False,
        "name": "frc1",
    },
    1: {
        "adv_model": 0,
        "adv_target": 27,
        "id": 1,
        "is_circle": True,
        "is_square": False,
        "name": "frc2",
    },
    2: {
        "adv_model": 0,
        "adv_target": 44,
        "id": 2,
        "is_circle": True,
        "is_square": False,
        "name": "frc3",
    },
    3: {
        "adv_model": 0,
        "adv_target": 17,
        "id": 3,
        "is_circle": True,
        "is_square": False,
        "name": "frc4",
    },
    4: {
        "adv_model": 0,
        "adv_target": 85,
        "id": 4,
        "is_circle": True,
        "is_square": False,
        "name": "frc5",
    },
    5: {
        "adv_model": 0,
        "adv_target": 73,
        "id": 5,
        "is_circle": True,
        "is_square": False,
        "name": "frc6",
    },
    6: {
        "adv_model": 0,
        "adv_target": 78,
        "id": 6,
        "is_circle": True,
        "is_square": False,
        "name": "frc7",
    },
    7: {
        "adv_model": 0,
        "adv_target": 1,
        "id": 7,
        "is_circle": True,
        "is_square": False,
        "name": "frc8",
    },
    8: {
        "adv_model": 0,
        "adv_target": 64,
        "id": 8,
        "is_circle": True,
        "is_square": False,
        "name": "frc9",
    },
    9: {
        "adv_model": 0,
        "adv_target": 33,
        "id": 9,
        "is_circle": True,
        "is_square": False,
        "name": "frc10",
    },
    10: {
        "adv_model": 0,
        "adv_target": 53,
        "id": 10,
        "is_circle": False,
        "is_square": True,
        "name": "frs1",
    },
    11: {
        "adv_model": 0,
        "adv_target": 27,
        "id": 11,
        "is_circle": False,
        "is_square": True,
        "name": "frs2",
    },
    12: {
        "adv_model": 0,
        "adv_target": 44,
        "id": 12,
        "is_circle": False,
        "is_square": True,
        "name": "frs3",
    },
    13: {
        "adv_model": 0,
        "adv_target": 17,
        "id": 13,
        "is_circle": False,
        "is_square": True,
        "name": "frs4",
    },
    14: {
        "adv_model": 0,
        "adv_target": 85,
        "id": 14,
        "is_circle": False,
        "is_square": True,
        "name": "frs5",
    },
    15: {
        "adv_model": 0,
        "adv_target": 73,
        "id": 15,
        "is_circle": False,
        "is_square": True,
        "name": "frs6",
    },
    16: {
        "adv_model": 0,
        "adv_target": 78,
        "id": 16,
        "is_circle": False,
        "is_square": True,
        "name": "frs7",
    },
    17: {
        "adv_model": 0,
        "adv_target": 1,
        "id": 17,
        "is_circle": False,
        "is_square": True,
        "name": "frs8",
    },
    18: {
        "adv_model": 0,
        "adv_target": 64,
        "id": 18,
        "is_circle": False,
        "is_square": True,
        "name": "frs9",
    },
    19: {
        "adv_model": 0,
        "adv_target": 33,
        "id": 19,
        "is_circle": False,
        "is_square": True,
        "name": "frs10",
    },
    20: {
        "adv_model": 1,
        "adv_target": 53,
        "id": 20,
        "is_circle": True,
        "is_square": False,
        "name": "rrc1",
    },
    21: {
        "adv_model": 1,
        "adv_target": 27,
        "id": 21,
        "is_circle": True,
        "is_square": False,
        "name": "rrc2",
    },
    22: {
        "adv_model": 1,
        "adv_target": 44,
        "id": 22,
        "is_circle": True,
        "is_square": False,
        "name": "rrc3",
    },
    23: {
        "adv_model": 1,
        "adv_target": 17,
        "id": 23,
        "is_circle": True,
        "is_square": False,
        "name": "rrc4",
    },
    24: {
        "adv_model": 1,
        "adv_target": 85,
        "id": 24,
        "is_circle": True,
        "is_square": False,
        "name": "rrc5",
    },
    25: {
        "adv_model": 1,
        "adv_target": 73,
        "id": 25,
        "is_circle": True,
        "is_square": False,
        "name": "rrc6",
    },
    26: {
        "adv_model": 1,
        "adv_target": 78,
        "id": 26,
        "is_circle": True,
        "is_square": False,
        "name": "rrc7",
    },
    27: {
        "adv_model": 1,
        "adv_target": 1,
        "id": 27,
        "is_circle": True,
        "is_square": False,
        "name": "rrc8",
    },
    28: {
        "adv_model": 1,
        "adv_target": 64,
        "id": 28,
        "is_circle": True,
        "is_square": False,
        "name": "rrc9",
    },
    29: {
        "adv_model": 1,
        "adv_target": 33,
        "id": 29,
        "is_circle": True,
        "is_square": False,
        "name": "rrc10",
    },
    30: {
        "adv_model": 1,
        "adv_target": 53,
        "id": 30,
        "is_circle": False,
        "is_square": True,
        "name": "rrs1",
    },
    31: {
        "adv_model": 1,
        "adv_target": 27,
        "id": 31,
        "is_circle": False,
        "is_square": True,
        "name": "rrs2",
    },
    32: {
        "adv_model": 1,
        "adv_target": 44,
        "id": 32,
        "is_circle": False,
        "is_square": True,
        "name": "rrs3",
    },
    33: {
        "adv_model": 1,
        "adv_target": 17,
        "id": 33,
        "is_circle": False,
        "is_square": True,
        "name": "rrs4",
    },
    34: {
        "adv_model": 1,
        "adv_target": 85,
        "id": 34,
        "is_circle": False,
        "is_square": True,
        "name": "rrs5",
    },
    35: {
        "adv_model": 1,
        "adv_target": 73,
        "id": 35,
        "is_circle": False,
        "is_square": True,
        "name": "rrs6",
    },
    36: {
        "adv_model": 1,
        "adv_target": 78,
        "id": 36,
        "is_circle": False,
        "is_square": True,
        "name": "rrs7",
    },
    37: {
        "adv_model": 1,
        "adv_target": 1,
        "id": 37,
        "is_circle": False,
        "is_square": True,
        "name": "rrs8",
    },
    38: {
        "adv_model": 1,
        "adv_target": 64,
        "id": 38,
        "is_circle": False,
        "is_square": True,
        "name": "rrs9",
    },
    39: {
        "adv_model": 1,
        "adv_target": 33,
        "id": 39,
        "is_circle": False,
        "is_square": True,
        "name": "rrs10",
    },
    40: {
        "adv_model": 2,
        "adv_target": 53,
        "id": 40,
        "is_circle": True,
        "is_square": False,
        "name": "smc1",
    },
    41: {
        "adv_model": 2,
        "adv_target": 27,
        "id": 41,
        "is_circle": True,
        "is_square": False,
        "name": "smc2",
    },
    42: {
        "adv_model": 2,
        "adv_target": 44,
        "id": 42,
        "is_circle": True,
        "is_square": False,
        "name": "smc3",
    },
    43: {
        "adv_model": 2,
        "adv_target": 17,
        "id": 43,
        "is_circle": True,
        "is_square": False,
        "name": "smc4",
    },
    44: {
        "adv_model": 2,
        "adv_target": 85,
        "id": 44,
        "is_circle": True,
        "is_square": False,
        "name": "smc5",
    },
    45: {
        "adv_model": 2,
        "adv_target": 73,
        "id": 45,
        "is_circle": True,
        "is_square": False,
        "name": "smc6",
    },
    46: {
        "adv_model": 2,
        "adv_target": 78,
        "id": 46,
        "is_circle": True,
        "is_square": False,
        "name": "smc7",
    },
    47: {
        "adv_model": 2,
        "adv_target": 1,
        "id": 47,
        "is_circle": True,
        "is_square": False,
        "name": "smc8",
    },
    48: {
        "adv_model": 2,
        "adv_target": 64,
        "id": 48,
        "is_circle": True,
        "is_square": False,
        "name": "smc9",
    },
    49: {
        "adv_model": 2,
        "adv_target": 33,
        "id": 49,
        "is_circle": True,
        "is_square": False,
        "name": "smc10",
    },
    50: {
        "adv_model": 2,
        "adv_target": 53,
        "id": 50,
        "is_circle": False,
        "is_square": True,
        "name": "sms1",
    },
    51: {
        "adv_model": 2,
        "adv_target": 27,
        "id": 51,
        "is_circle": False,
        "is_square": True,
        "name": "sms2",
    },
    52: {
        "adv_model": 2,
        "adv_target": 44,
        "id": 52,
        "is_circle": False,
        "is_square": True,
        "name": "sms3",
    },
    53: {
        "adv_model": 2,
        "adv_target": 17,
        "id": 53,
        "is_circle": False,
        "is_square": True,
        "name": "sms4",
    },
    54: {
        "adv_model": 2,
        "adv_target": 85,
        "id": 54,
        "is_circle": False,
        "is_square": True,
        "name": "sms5",
    },
    55: {
        "adv_model": 2,
        "adv_target": 73,
        "id": 55,
        "is_circle": False,
        "is_square": True,
        "name": "sms6",
    },
    56: {
        "adv_model": 2,
        "adv_target": 78,
        "id": 56,
        "is_circle": False,
        "is_square": True,
        "name": "sms7",
    },
    57: {
        "adv_model": 2,
        "adv_target": 1,
        "id": 57,
        "is_circle": False,
        "is_square": True,
        "name": "sms8",
    },
    58: {
        "adv_model": 2,
        "adv_target": 64,
        "id": 58,
        "is_circle": False,
        "is_square": True,
        "name": "sms9",
    },
    59: {
        "adv_model": 2,
        "adv_target": 33,
        "id": 59,
        "is_circle": False,
        "is_square": True,
        "name": "sms10",
    },
}