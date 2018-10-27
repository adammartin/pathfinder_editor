import math


ALIGNMENTS = {
    'Neutral': {'Vector': {'x': 0, 'y': 0},
                'angle_min': 0, 'angle_max': 0, 'radius': 0.4},
    'Chaotic Good': {'Vector': {'x': 0.707106769, 'y': 0.707106769},
                     'angle_min': 0, 'angle_max': 45},
    'Neutral Good': {'Vector': {'x': 0, 'y': 1},
                     'angle_min': 45, 'angle_max': 90},
    'Lawful Good': {'Vector': {'x': -0.707106769, 'y': 0.707106769},
                    'angle_min': 90, 'angle_max': 135},
    'Lawful Neutral': {'Vector': {'x': -1, 'y': 0},
                       'angle_min': 135, 'angle_max': 180},
    'Lawful Evil': {'Vector': {'x': -0.707106769, 'y': -0.707106769},
                    'angle_min': 180, 'angle_max': 225},
    'Neutral Evil': {'Vector': {'x': 0, 'y': -1},
                     'angle_min': 225, 'angle_max': 270},
    'Chaotic Evil': {'Vector': {'x': 0.707106769, 'y': -0.707106769},
                     'angle_min': 270, 'angle_max': 315},
    'Chaotic Neutral': {'Vector': {'x': 1, 'y': 0},
                        'angle_min': 315, 'angle_max': 360},
}


class AlignmentInfo():
    def __init__(self, alignment_block):
        self._align_block = alignment_block

    def alignment(self):
        x_axis = self._align_block['Vector']['x']
        y_axis = self._align_block['Vector']['y']
        return _calculate_alignment(x_axis, y_axis)

    def update_alignment(self, value):
        if value != self.alignment():
            vector = ALIGNMENTS[value]['Vector']
            self._align_block['Vector'] = vector
            self._align_block['m_History'][-1]['Position'] = vector


def _calculate_angle(x_axis, y_axis):
    # CCW Angle starting east
    angle = (math.atan2(y_axis, x_axis) * 180 / math.pi) - 22.5
    if angle < 0:
        angle += 360
    return angle


def _calculate_alignment(x_axis, y_axis):
    angle = _calculate_angle(x_axis, y_axis)
    radius = math.sqrt(x_axis * x_axis + y_axis * y_axis)
    for align, data in ALIGNMENTS.items():
        if 'radius' in data and radius <= data['radius']:
            return align
        elif angle >= data['angle_min'] and angle < data['angle_max']:
            return align
    return 'UNKOWN'
