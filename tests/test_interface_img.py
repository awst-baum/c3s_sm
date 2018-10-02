# -*- coding: utf-8 -*-

from c3s_sm_reader.interface import C3SImg
import os
import numpy.testing as nptest

def test_C33Ts_tcdr_combined_daily():


    file = os.path.join(os.path.join(os.path.dirname(__file__),
                        'test-data', 'img', 'TCDR', '060_dailyImages', 'combined',
                        'C3S-SOILMOISTURE-L3S-SSMV-COMBINED-DAILY-20140101000000-TCDR-v201801.0.0.nc'))


    ds = C3SImg(file, mode='r', parameters='sm', array_1D=False)
    image= ds.read()

    nptest.assert_almost_equal(image.data['sm'][167, 785], 0.34659, 4)
    assert(image.metadata['sm']['long_name'] == 'Volumetric Soil Moisture')
    #assert(file_meta['creator_name'] == 'Earth Observation Data Center (EODC)')



def test_C33Ts_tcdr_active_monthly():

    file = os.path.join(os.path.join(os.path.dirname(__file__),
                        'test-data', 'img', 'TCDR', '061_monthlyImages', 'active',
                        'C3S-SOILMOISTURE-L3S-SSMS-ACTIVE-MONTHLY-20140101000000-TCDR-v201801.0.0.nc'))


    ds = C3SImg(file, mode='r', parameters='sm', array_1D=False)
    image = ds.read()

    nptest.assert_almost_equal(image.data['sm'][167, 785], 47.69982, 4)
    assert(image.metadata['sm']['_FillValue'] == -9999.)
    assert(image.metadata['sm']['long_name'] == 'Percent of Saturation Soil Moisture')
    #assert(file_meta['creator_name'] == 'Earth Observation Data Center (EODC)')


def test_C33Ts_tcdr_passive_decadal():
    file = os.path.join(os.path.join(os.path.dirname(__file__),
                        'test-data', 'img', 'TCDR', '062_dekadalImages', 'passive',
                        'C3S-SOILMOISTURE-L3S-SSMV-PASSIVE-DEKADAL-20140101000000-TCDR-v201801.0.0.nc'))


    ds = C3SImg(file, mode='r', parameters='sm', array_1D=False)
    image = ds.read()

    nptest.assert_almost_equal(image['sm'][167, 784], 0.50875, 4)
    assert(image.metadata['sm']['long_name'] == 'Volumetric Soil Moisture')
    #assert(image.metadata['creator_name'] == 'Earth Observation Data Center (EODC)')

################################################################################

def test_C33Ts_icdr_combined_daily():
    file = os.path.join(os.path.join(os.path.dirname(__file__),
                        'test-data', 'img', 'ICDR', '060_dailyImages', 'combined',
                        'C3S-SOILMOISTURE-L3S-SSMV-COMBINED-DAILY-20170701000000-ICDR-v201706.0.0.nc'))


    ds = C3SImg(file, mode='r', parameters='sm', array_1D=False)
    image = ds.read()

    nptest.assert_almost_equal(image.data['sm'][167, 785], 0.14548, 4)
    assert(image.metadata['sm']['long_name'] == 'Volumetric Soil Moisture')
    #assert(image['creator_name'] == 'Earth Observation Data Center (EODC)')



def test_C33Ts_icdr_active_monthly():

    file = os.path.join(os.path.join(os.path.dirname(__file__),
                        'test-data', 'img', 'ICDR', '061_monthlyImages', 'active',
                        'C3S-SOILMOISTURE-L3S-SSMS-ACTIVE-MONTHLY-20170701000000-ICDR-v201706.0.0.nc'))


    ds = C3SImg(file, mode='r', parameters='sm', array_1D=False)
    image = ds.read()

    nptest.assert_almost_equal(image.data['sm'][167, 785], 65.00162, 4)
    assert(image.metadata['sm']['_FillValue'] == -9999.)
    assert(image.metadata['sm']['long_name'] == 'Percent of Saturation Soil Moisture')
    #assert(file_meta['creator_name'] == 'Earth Observation Data Center (EODC)')


def test_C33Ts_icdr_passive_decadal():
    file = os.path.join(os.path.join(os.path.dirname(__file__),
                        'test-data', 'img', 'ICDR', '062_dekadalImages', 'passive',
                        'C3S-SOILMOISTURE-L3S-SSMV-PASSIVE-DEKADAL-20170701000000-ICDR-v201706.0.0.nc'))


    ds = C3SImg(file, mode='r', parameters='sm', array_1D=False)
    image = ds.read()

    nptest.assert_almost_equal(image.data['sm'][167, 785], 0.21000, 4)
    assert(image.metadata['sm']['long_name'] == 'Volumetric Soil Moisture')
    #assert(image.metadata['creator_name'] == 'Earth Observation Data Center (EODC)')


if __name__ == '__main__':
    test_C33Ts_tcdr_combined_daily()
    test_C33Ts_tcdr_active_monthly()
    test_C33Ts_tcdr_passive_decadal()

    test_C33Ts_icdr_combined_daily()
    test_C33Ts_icdr_active_monthly()
    test_C33Ts_icdr_passive_decadal()
