# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 18:03:26 2020

@author: skjerns
"""
import os
import numpy as np
import mat73
import unittest



class Testing(unittest.TestCase):

    def setUp(self):
        for i in range(1,4):
            file = 'testfile{}.mat'.format(i)
            if not os.path.exists(file):
                file = os.path.join('./tests', file)
            self.__setattr__ ('testfile{}'.format(i), file)

    def test_file1_noattr(self):
        """
        Test each default MATLAB type loads correctl
        """
        d = mat73.loadmat(self.testfile1)
        data = d['data']
        
        assert len(d)==3
        assert len(d.keys())==3
        assert len(data)==28
        assert data['arr_two_three'].shape==(3,2)
        np.testing.assert_allclose(d['secondvar'], [1,2,3,4])
        np.testing.assert_array_equal(data['arr_bool'], np.array([True,True,False]))
        assert data['arr_bool'].dtype==bool
        assert data['arr_char']=='test'
        np.testing.assert_array_equal(data['arr_double'], np.array([1.1,1.2,0.3],dtype=np.float64))
        assert data['arr_double'].dtype==np.float64
        np.testing.assert_array_equal(data['arr_float'], np.array([[1.1,2],[1.2,3],[0.3,4]],dtype=np.float32).T)
        np.testing.assert_array_equal(data['arr_nan'], np.array([np.nan,np.nan]))
        assert data['bool_']== False
        np.testing.assert_array_equal(data['cell_'][0], np.array([1.1,2.2]))
        np.testing.assert_array_equal(data['cell_'][1], False)
        np.testing.assert_array_equal(data['cell_'][2], [False, True])
        np.testing.assert_array_equal(data['cell_'][3], [1.1])
        np.testing.assert_array_equal(data['cell_'][4], [0])
        np.testing.assert_array_equal(data['cell_'][5], 'test')
        np.testing.assert_array_equal(data['cell_'][6][0], 'subcell')
        np.testing.assert_array_equal(data['cell_'][6][1], 0)
        np.testing.assert_array_equal(data['cell_char_'], [['Smith', 'Chung', 'Morales'], ['Sanchez','Peterson','Adams']])
        assert data['char_']== 'x'
        np.testing.assert_array_equal(data['complex_'], np.array([2+3j]))
        np.testing.assert_array_equal(data['complex2_'], np.array([123456789.123456789+987654321.987654321j]))
        np.testing.assert_array_equal(data['complex3_'], np.array([8.909089035006170e-04 + 0.000000000000000e+00j]))

        assert data['double_']==0.1
        assert data['double_'].dtype==np.float64
        assert data['int16_']==16
        assert data['int16_'].dtype==np.int16
        assert data['int32_']==1115
        assert data['int32_'].dtype==np.int32  
        assert data['int64_']==65243
        assert data['int64_'].dtype==np.int64 
        assert data['int8_']==2
        assert data['int8_'].dtype==np.int8 
        np.testing.assert_array_equal(data['nan_'], np.nan)
        assert data['nan_'].dtype==np.float64
        assert data['single_']==np.array(0.1, dtype=np.float32)
        assert data['single_'].dtype==np.float32
        assert data['string_']=='tasdfasdf'
        assert data['uint8_']==2
        assert data['uint8_'].dtype==np.uint8
        assert data['uint16_']==12
        assert data['uint16_'].dtype==np.uint16
        assert data['uint32_']==5452
        assert data['uint32_'].dtype==np.uint32       
        assert data['uint64_']==32563
        assert data['uint64_'].dtype==np.uint64
        assert len(data['struct_'])==1
        np.testing.assert_array_equal(data['struct_']['test'],[1,2,3,4])
        assert len(data['struct2_'])==2
        assert len(data['structarr_'])==3
        assert data['structarr_'][0] == {'f1': ['some text'], 'f2': ['v1']}
        assert data['structarr_'][1]['f2'] == ['v2']
        assert data['structarr_'][2]['f2'] == ['v3']
        assert d['keys'] == 'must_not_overwrite'

        with self.assertRaises(KeyError):
            d.structarr_


    def test_file1_withattr(self):
        """
        Test each default MATLAB type loads correctl
        """
        d = mat73.loadmat(self.testfile1, use_attrdict=True)
        data = d['data']
        
        assert len(d)==3
        assert len(d.keys())==3
        assert len(data)==28
        assert data['arr_two_three'].shape==(3,2)
        np.testing.assert_allclose(d['secondvar'], [1,2,3,4])
        np.testing.assert_array_equal(data['arr_bool'], np.array([True,True,False]))
        assert data['arr_bool'].dtype==bool
        assert data['arr_char']=='test'
        np.testing.assert_array_equal(data['arr_double'], np.array([1.1,1.2,0.3],dtype=np.float64))
        assert data['arr_double'].dtype==np.float64
        np.testing.assert_array_equal(data['arr_float'], np.array([[1.1,2],[1.2,3],[0.3,4]],dtype=np.float32).T)
        np.testing.assert_array_equal(data['arr_nan'], np.array([np.nan,np.nan]))
        assert data['bool_']== False
        np.testing.assert_array_equal(data['cell_'][0], np.array([1.1,2.2]))
        np.testing.assert_array_equal(data['cell_'][1], False)
        np.testing.assert_array_equal(data['cell_'][2], [False, True])
        np.testing.assert_array_equal(data['cell_'][3], [1.1])
        np.testing.assert_array_equal(data['cell_'][4], [0])
        np.testing.assert_array_equal(data['cell_'][5], 'test')
        np.testing.assert_array_equal(data['cell_'][6][0], 'subcell')
        np.testing.assert_array_equal(data['cell_'][6][1], 0)
        np.testing.assert_array_equal(data['cell_char_'], [['Smith', 'Chung', 'Morales'], ['Sanchez','Peterson','Adams']])
        assert data['char_']== 'x'
        np.testing.assert_array_equal(data['complex_'], np.array([2+3j]))
        np.testing.assert_array_equal(data['complex2_'], np.array([123456789.123456789+987654321.987654321j]))
        np.testing.assert_array_equal(data['complex3_'], np.array([8.909089035006170e-04 + 0.000000000000000e+00j]))

        assert data['double_']==0.1
        assert data['double_'].dtype==np.float64
        assert data['int16_']==16
        assert data['int16_'].dtype==np.int16
        assert data['int32_']==1115
        assert data['int32_'].dtype==np.int32  
        assert data['int64_']==65243
        assert data['int64_'].dtype==np.int64 
        assert data['int8_']==2
        assert data['int8_'].dtype==np.int8 
        np.testing.assert_array_equal(data['nan_'], np.nan)
        assert data['nan_'].dtype==np.float64
        assert data['single_']==np.array(0.1, dtype=np.float32)
        assert data['single_'].dtype==np.float32
        assert data['string_']=='tasdfasdf'
        assert data['uint8_']==2
        assert data['uint8_'].dtype==np.uint8
        assert data['uint16_']==12
        assert data['uint16_'].dtype==np.uint16
        assert data['uint32_']==5452
        assert data['uint32_'].dtype==np.uint32       
        assert data['uint64_']==32563
        assert data['uint64_'].dtype==np.uint64
        assert len(data['struct_'])==1
        np.testing.assert_array_equal(data['struct_']['test'],[1,2,3,4])
        assert len(data['struct2_'])==2
        assert len(data['structarr_'])==3
        assert data['structarr_'][0] == {'f1': ['some text'], 'f2': ['v1']}
        assert data['structarr_'][1]['f2'] == ['v2']
        assert data['structarr_'][2]['f2'] == ['v3']


        ## now do the same with attrdict
        data = d.data

        assert len(d)==3
        assert len(data)==28
        assert data.arr_two_three.shape==(3,2)
        np.testing.assert_allclose(d.secondvar, [1,2,3,4])
        np.testing.assert_array_equal(data.arr_bool, np.array([True,True,False]))
        assert data.arr_bool.dtype==bool
        assert data.arr_char=='test'
        np.testing.assert_array_equal(data.arr_double, np.array([1.1,1.2,0.3],dtype=np.float64))
        assert data.arr_double.dtype==np.float64
        np.testing.assert_array_equal(data.arr_float, np.array([[1.1,2],[1.2,3],[0.3,4]],dtype=np.float32).T)
        np.testing.assert_array_equal(data.arr_nan, np.array([np.nan,np.nan]))
        assert data.bool_== False
        np.testing.assert_array_equal(data.cell_[0], np.array([1.1,2.2]))
        np.testing.assert_array_equal(data.cell_[1], False)
        np.testing.assert_array_equal(data.cell_[2], [False, True])
        np.testing.assert_array_equal(data.cell_[3], [1.1])
        np.testing.assert_array_equal(data.cell_[4], [0])
        np.testing.assert_array_equal(data.cell_[5], 'test')
        np.testing.assert_array_equal(data.cell_[6][0], 'subcell')
        np.testing.assert_array_equal(data.cell_[6][1], 0)
        np.testing.assert_array_equal(data.cell_char_, [['Smith', 'Chung', 'Morales'], ['Sanchez','Peterson','Adams']])
        assert data.char_== 'x'
        np.testing.assert_array_equal(data.complex_, np.array([2+3j]))
        np.testing.assert_array_equal(data.complex2_, np.array([123456789.123456789+987654321.987654321j]))
        np.testing.assert_array_equal(data.complex3_, np.array([8.909089035006170e-04 + 0.000000000000000e+00j]))

        assert data.double_==0.1
        assert data.double_.dtype==np.float64
        assert data.int16_==16
        assert data.int16_.dtype==np.int16
        assert data.int32_==1115
        assert data.int32_.dtype==np.int32  
        assert data.int64_==65243
        assert data.int64_.dtype==np.int64 
        assert data.int8_==2
        assert data.int8_.dtype==np.int8 
        np.testing.assert_array_equal(data.nan_, np.nan)
        assert data.nan_.dtype==np.float64
        assert data.single_==np.array(0.1, dtype=np.float32)
        assert data.single_.dtype==np.float32
        assert data.string_=='tasdfasdf'
        assert data.uint8_==2
        assert data.uint8_.dtype==np.uint8
        assert data.uint16_==12
        assert data.uint16_.dtype==np.uint16
        assert data.uint32_==5452
        assert data.uint32_.dtype==np.uint32       
        assert data.uint64_==32563
        assert data.uint64_.dtype==np.uint64
        assert len(data.struct_)==1
        np.testing.assert_array_equal(data.struct_.test,[1,2,3,4])
        assert len(data.struct2_)==2
        assert len(data.structarr_)==3
        assert data.structarr_[0] == {'f1': ['some text'], 'f2': ['v1']}
        assert data.structarr_[1].f2 == ['v2']
        assert data.structarr_[2].f2 == ['v3']
        assert d['keys'] == 'must_not_overwrite'
        assert d.keys!='must_not_overwrite'



    def test_file2(self):
        """
        Test that complex numbers are loaded correctly
        """
        d = mat73.loadmat(self.testfile2)
        raw1 = d['raw1']
        assert raw1['label'] == ['']*5
        assert raw1['speakerType'] == ['main']*5
        np.testing.assert_array_equal(raw1['channel'],[1,2,3,4,5])
        np.testing.assert_allclose(raw1['measGain'],[-1.0160217,-0.70729065,-1.2158508,0.68839645,2.464653])
        for i in range(5):
            assert np.isclose(np.sum(raw1['h'][i]),-0.0007341067459898744)
    
        np.testing.assert_array_almost_equal(raw1['HSmooth'][0][2], [ 0.001139-4.233492e-04j,  0.00068 +8.927040e-06j,
        0.002382-7.647651e-04j, -0.012677+3.767829e-03j])


    def test_file3(self):
        """
        Test larger complex numbers are also loaded
        """
        d = mat73.loadmat(self.testfile3)
        raw1 = d['raw1']
        assert raw1['label'] == ['']*5
        assert raw1['speakerType'] == ['main']*5
        np.testing.assert_array_equal(raw1['channel'],[1,2,3,4,5])
        np.testing.assert_allclose(raw1['measGain'],[-1.0160217,-0.70729065,-1.2158508,0.68839645,2.464653])
        for i in range(5):
            assert np.isclose(np.sum(raw1['h'][i]),-0.019355850366449)
        for i in range(5):
            assert np.isclose(np.sum(raw1['HSmooth'][i]),-0.019355850366449)
        

if __name__ == '__main__':  
    unittest.main()





