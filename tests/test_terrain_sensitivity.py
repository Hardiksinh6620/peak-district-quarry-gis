import unittest
from examples.terrain_sensitivity import audit

class TerrainAuditTests(unittest.TestCase):
    def complete(self):
        return {'elevation_source':'x','horizontal_crs':'y','vertical_units':'metres','cell_size':10,'slope_units':'degrees','hillshade_azimuth':315,'hillshade_altitude':45,'observer_height':1.7,'target_height':0}
    def test_complete_inventory(self): self.assertTrue(audit(self.complete())['complete'])
    def test_missing_fields(self): self.assertIn('cell_size', audit({})['missing'])
    def test_invalid_angles(self):
        p=self.complete();p['hillshade_azimuth']=360;p['hillshade_altitude']=0
        self.assertEqual(audit(p)['invalid'],['hillshade_altitude','hillshade_azimuth'])
    def test_negative_heights_rejected(self):
        p=self.complete();p['observer_height']=-1
        self.assertIn('observer_height',audit(p)['invalid'])
    def test_boolean_numeric_rejected(self):
        p=self.complete();p['cell_size']=True
        self.assertIn('cell_size',audit(p)['invalid'])

if __name__=='__main__': unittest.main()
