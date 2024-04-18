"""Educational terrain-parameter inventory; no original raster is reproduced."""
import json

REQUIRED = {
    'elevation_source', 'horizontal_crs', 'vertical_units', 'cell_size',
    'slope_units', 'hillshade_azimuth', 'hillshade_altitude',
    'observer_height', 'target_height'
}

def audit(parameters):
    missing = sorted(REQUIRED - set(parameters))
    invalid = []
    if 'hillshade_azimuth' in parameters and not 0 <= parameters['hillshade_azimuth'] < 360:
        invalid.append('hillshade_azimuth')
    if 'hillshade_altitude' in parameters and not 0 < parameters['hillshade_altitude'] <= 90:
        invalid.append('hillshade_altitude')
    for field in ['cell_size', 'observer_height', 'target_height']:
        if field in parameters and (not isinstance(parameters[field], (int, float)) or isinstance(parameters[field], bool) or parameters[field] < 0):
            invalid.append(field)
    return {'complete': not missing and not invalid, 'missing': missing, 'invalid': sorted(set(invalid)), 'original_analysis_reproduced': False}

if __name__ == '__main__':
    example = {'elevation_source':'example DEM','horizontal_crs':'example projected CRS','vertical_units':'metres','cell_size':10,'slope_units':'degrees','hillshade_azimuth':315,'hillshade_altitude':45,'observer_height':1.7,'target_height':0}
    print(json.dumps(audit(example), indent=2))
