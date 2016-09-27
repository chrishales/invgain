from taskinit import *

# Copyright (c) 2015, Christopher A. Hales
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * The NAMES OF ITS CONTRIBUTORS may not be used to endorse or promote
#       products derived from this software without specific prior written
#       permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL C. A. HALES BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA,
# OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# HISTORY:
#   1.0  16Sep2015  Initial version.
#   1.1  27Sep2016  Fixed typos, no functionality change
#

def invgain(caltable,field,spw,scan,obsid):

    #
    # Task invgain
    #
    #    Invert gain solutions, overwriting caltable.
    #    Christopher A. Hales
    #
    #    Version 1.1 (tested with CASA Version 4.6.0)
    #    27 September 2016
    
    casalog.origin('invgain')
    
    selection=''
    if len(field)>0:
        if not field.isdigit():
            casalog.post('*** ERROR: This version does not support multiple FIELD_ID selection.', 'ERROR')
            casalog.post('*** ERROR: Exiting invgain.', 'ERROR')
            return
        
        selection=selection+'FIELD_ID=='+field+'&&'
    
    if len(spw)>0:
        if not spw.isdigit():
            casalog.post('*** ERROR: This version does not support multiple SPECTRAL_WINDOW_ID selection.', 'ERROR')
            casalog.post('*** ERROR: Exiting invgain.', 'ERROR')
            return
        
        selection=selection+'SPECTRAL_WINDOW_ID=='+spw+'&&'
    
    if len(scan)>0:
        if not scan.isdigit():
            casalog.post('*** ERROR: This version does not support multiple SCAN_NUMBER selection.', 'ERROR')
            casalog.post('*** ERROR: Exiting invgain.', 'ERROR')
            return
        
        selection=selection+'SCAN_NUMBER=='+scan+'&&'
    
    if len(obsid)>0:
        if not obsid.isdigit():
            casalog.post('*** ERROR: This version does not support multiple OBSERVATION_ID selection.', 'ERROR')
            casalog.post('*** ERROR: Exiting invgain.', 'ERROR')
            return
        
        selection=selection+'OBSERVATION_ID=='+obsid+'&&'
    
    tb.open(caltable,nomodify=False)
    
    if len(selection)>0:
        selection=selection[:-2]
        subt=tb.query(selection)
        temp=subt.getcol('CPARAM')
        subt.putcol('CPARAM',1/temp)
        subt.done()
    else:
        temp=tb.getcol('CPARAM')
        tb.putcol('CPARAM',1/temp)
    
    tb.done()
