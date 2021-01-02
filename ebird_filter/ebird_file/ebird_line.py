import datetime
from shapely.geometry import Point

class eBirdLine():
    """
    Utility class to get data from an eBird data file line.
    """
    def __init__(self, raw_line, headers):
        self.headers = headers
        self.raw_line = raw_line
        self.line_dict =  dict(zip(headers, raw_line.split('\t')))
    
    def get_field(self, name):
        return self.line_dict[name]
    
    def get_geo_point(self):
        lat = self.get_field('LATITUDE')
        lon = self.get_field('LONGITUDE')
        point = Point(float(lat), float(lon))
        return point
    
    def get_date(self):
        return datetime.datetime.strptime(self.get_field('OBSERVATION DATE'), "%Y-%m-%d")
    
    def get_common_name(self):
        return self.get_field('COMMON NAME')
    
    def get_unaccepted(self):
        return int(self.get_field('APPROVED'))
    
    def pretty_print(self):
        header_line = '\t'.join(self.headers)
        return '\n'.join([header_line, raw_line])
    
    def get_raw_line(self):
        return self.raw_line
        
