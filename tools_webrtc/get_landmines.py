#!/usr/bin/env python
# Copyright (c) 2015 The WebRTC project authors. All Rights Reserved.
#
# Use of this source code is governed by a BSD-style license
# that can be found in the LICENSE file in the root of the source
# tree. An additional intellectual property rights grant can be found
# in the file PATENTS.  All contributing project authors may
# be found in the AUTHORS file in the root of the source tree.

"""
This file emits the list of reasons why a particular build needs to be clobbered
(or a list of 'landmines').
"""

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
CHECKOUT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, os.pardir))
sys.path.insert(0, os.path.join(CHECKOUT_ROOT, 'build'))
import landmine_utils


platform = landmine_utils.platform  # pylint: disable=invalid-name


def print_landmines():  # pylint: disable=invalid-name
  """
  ALL LANDMINES ARE EMITTED FROM HERE.
  """
  # DO NOT add landmines as part of a regular CL. Landmines are a last-effort
  # bandaid fix if a CL that got landed has a build dependency bug and all bots
  # need to be cleaned up. If you're writing a new CL that causes build
  # dependency problems, fix the dependency problems instead of adding a
  # landmine.
  # See the Chromium version in src/build/get_landmines.py for usage examples.
  print 'Clobber to remove out/{Debug,Release}/args.gn (webrtc:5070)'
  if platform() == 'android':
    print ('Clobber to remove artifacts on Android causing lint errors after '
           'rolling in https://codereview.webrtc.org/2293863002')
    print ('Clobber to remove old AppRTCDemo artifacts after renaming to '
           'AppRTCMobile in https://codereview.webrtc.org/2373443005')
    print ('Clobber to fix Android x86/x64 builds after '
           'https://codereview.webrtc.org/1414343008/')
  if platform() == 'win':
    print 'Clobber to resolve some issues with corrupt .pdb files on bots.'
    print 'Clobber due to corrupt .pdb files (after #14623)'
    print 'Clobber due to Win 64-bit Debug linking error (crbug.com/668961)'
    print ('Clobber due to Win Clang Debug linking errors in '
           'https://codereview.webrtc.org/2786603002')
    print ('Clobber due to Win Debug linking errors in '
           'https://codereview.webrtc.org/2832063003/')
  if platform() == 'mac':
    # platform == 'ios' doesn't work since it assumes GYP_DEFINES is set, which
    # is no longer the case.
    print 'Clobber due to iOS compile errors (crbug.com/694721)'
    print 'Clobber to unblock https://codereview.webrtc.org/2709573003'
    print ('Clobber to fix https://codereview.webrtc.org/2709573003 after '
           'landing')
    print ('Clobber to fix https://codereview.webrtc.org/2767383005 before'
           'landing (changing rtc_executable -> rtc_test on iOS)')
    print ('Clobber to fix https://codereview.webrtc.org/2767383005 before'
           'landing (changing rtc_executable -> rtc_test on iOS)')
    print 'Another landmine for low_bandwidth_audio_test (webrtc:7430)'


def main():
  print_landmines()
  return 0


if __name__ == '__main__':
  sys.exit(main())
