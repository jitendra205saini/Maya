DEFAULT_DATA = {
# Buttons
'AddMarkerButtonDisplay':           'icon',
'AddMarkerButtonIconHover':            './maya/media/add_marker_hover.png',    
'AddMarkerButtonIconOff':              './maya/media/add_marker_off.png',
'AddMarkerButtonIconOn':               './maya/media/add_marker_off.png',
'AddMarkerButtonInfoText':             'ADD MARKER:\nAttaches a parameter marker to the current frame. Markers copy all parameter settings and apply them to all future frames, or until another marker is encountered.',
'AddMarkerButtonState':           False,
'AudioDisplay':             'text', 
'AudioInfoText':             'ENABLE REAL-TIME AUDIO:\nAdds audio from the input video during preview playback. If you are unable to maintain the input video frame rate, the audio will lag.',   
'AudioState':               False,
'AudioText':                'Enable Audio',      
'AutoSwapState':            False,
'ClearFacesDisplay':        'text', 
'ClearFacesIcon':            './maya/media/tarfacedel.png',
'ClearFacesIconHover':      './maya/media/rec.png',
'ClearFacesIconOff':        './maya/media/rec.png',
'ClearFacesIconOn':         './maya/media/rec.png',
'ClearFacesInfoText':             'REMOVE FACES:\nRemove all currently found faces.',
'ClearFacesState':          False,      
'ClearFacesText':           'Clear Faces',   
'ClearmemState':            False,
'DefaultParamsButtonDisplay':           'text',
'DefaultParamsButtonInfoText':             'LOAD DEFAULT PARAMETERS:\nLoad the Rope default parameters for this column.',
'DefaultParamsButtonState':           False,
'DefaultParamsButtonText':           'Load Defaults',
'DelEmbedDisplay':          'text', 
'DelEmbedIconHover':        './maya/media/rec.png',      
'DelEmbedIconOff':          './maya/media/rec.png',
'DelEmbedIconOn':           './maya/media/rec.png',
'DelEmbedInfoText':             'DELETE EMBEDDING:\nDelete the currently selected embedding',
'DelEmbedState':            False,          
'DelEmbedText':             'Delete Emb',  
'DelMarkerButtonDisplay':           'icon',
'DelMarkerButtonIconHover':            './maya/media/remove_marker_hover.png',    
'DelMarkerButtonIconOff':              './maya/media/remove_marker_off.png',
'DelMarkerButtonIconOn':               './maya/media/remove_marker_off.png',
'DelMarkerButtonInfoText':             'REMOVE MARKER:\nRemoves the parameter marker from the current frame.',
'DelMarkerButtonState':           False,
'FindFacesDisplay':         'text', 
'FindFacesIcon':         './maya/media/tarface.png',
'FindFacesIconHover':       './maya/media/rec.png',
'FindFacesIconOff':         './maya/media/rec.png',
'FindFacesIconOn':          './maya/media/rec.png',
'FindFacesInfoText':             'FIND FACES:\nFinds all new faces in the current frame.',
'FindFacesState':           False,  
'FindFacesText':            'Find Faces',  
'ImgDockState':             False,
'ImgVidMode':               'Videos', 
'ImgVidState':              False,
'LoadParamsButtonDisplay':           'text',
'LoadParamsButtonInfoText':             'LOAD SAVED PARAMETERS:\nLoads all parameters from this column if they have been previously saved. ',
'LoadParamsButtonState':           False,
'LoadParamsButtonText':           'Load Params',
'LoadSFacesDisplay':         'both', 
'LoadSFacesIcon':            './maya/media/save.png',
'LoadSFacesIconHover':        './maya/media/save.png',     
'LoadSFacesIconOff':          './maya/media/save.png',
'LoadSFacesIconOn':           './maya/media/save.png',
'LoadSFacesInfoText':             'SELECT SOURCE FACES FOLDER:\nSelects and loads Source Faces from Folder. Make sure the folder only contains <good> images.',
'LoadSFacesState':          False,
'LoadSFacesText':           'Select Faces Folder',  
'LoadTVideosDisplay':         'both', 
'LoadTVideosIconHover':        './maya/media/save.png', 
'LoadTVideosIconOff':          './maya/media/save.png',
'LoadTVideosIconOn':           './maya/media/save.png',
'LoadTVideosInfoText':             'SELECT INPUT VIDEOS/IMAGES FOLDER:\nSelect and load media from folder.',
'LoadTVideosState':         False,    
'LoadTVideosText':           'Select Videos Folder',  
'MaskViewDisplay':         'text',   
'MaskViewInfoText':             'SHOW MASKS:\nDisplays the mask for a face side-by-side with the face. Useful for understanding the masking behaviors and results.',
'MaskViewState':            False,    
'MaskViewText':           'Show Mask', 
'NextMarkerButtonDisplay':           'icon',
'NextMarkerButtonIconHover':            './maya/media/next_marker_hover.png',    
'NextMarkerButtonIconOff':              './maya/media/next_marker_off.png',
'NextMarkerButtonIconOn':               './maya/media/next_marker_off.png',
'NextMarkerButtonInfoText':             'NEXT MARKER:\nMove to the next marker.',
'NextMarkerButtonState':           False,
'OutputFolderDisplay':         'both', 
'OutputFolderIconHover':        './maya/media/save.png', 
'OutputFolderIconOff':          './maya/media/save.png',
'OutputFolderIconOn':           './maya/media/save.png',
'OutputFolderInfoText':             'SELECT SAVE FOLDER:\nSelect folder for saved videos and images.',
'OutputFolderState':        False,   
'OutputFolderText':           'Select Output Folder',  
'PerfTestState':            False,
'PlayDisplay':              'icon',   
'PlayIconHover':            './maya/media/play_hover.png',
'PlayIconOff':              './maya/media/play_off.png',
'PlayIconOn':               './maya/media/play_on.png',
'PlayInfoText':             'PLAY:\nPlays the video. Press again to stop playing',
'PlayState':                False,
'PrevMarkerButtonDisplay':           'icon',
'PrevMarkerButtonIconHover':            './maya/media/previous_marker_hover.png',    
'PrevMarkerButtonIconOff':              './maya/media/previous_marker_off.png',
'PrevMarkerButtonIconOn':               './maya/media/previous_marker_off.png',
'PrevMarkerButtonInfoText':             'PREVIOUS MARKER:\nMove to the previous marker.',
'PrevMarkerButtonState':           False,
'RecordDisplay':            'icon',     
'RecordIconHover':          './maya/media/rec_hover.png',
'RecordIconOff':            './maya/media/rec_off.png',
'RecordIconOn':             './maya/media/rec_on.png',
'RecordInfoText':             'RECORD:\nArms the PLAY button for recording. Press RECORD, then PLAY to record. Press PLAY again to stop recording.',  
'RecordState':              False,       
'SaveImageState':           False,
'SaveParamsButtonDisplay':           'text',
'SaveParamsButtonInfoText':             'SAVE PARAMETERS:\nSaves all parameters in this column.',
'SaveParamsButtonState':            False,
'SaveParamsButtonText':             'Save Params',
'StartRopeDisplay':                 'both', 
'StartRopeIconHover':               './maya/media/maya.png',    
'StartRopeIconOff':                 './maya/media/maya.png',
'StartRopeIconOn':                  './maya/media/maya.png',
'StartRopeInfoText':                'STARTS MAYA:\nStarts up the Maya application.',
'StartRopeState':                   False,    
'StartRopeText':                    'Start Maya',  
'SwapFacesDisplay':                 'text', 
'SwapFacesInfoText':                'SWAP:\nSwap assigned Source Faces and Target Faces.',
'SwapFacesState':                   False,          
'SwapFacesText':                    'Swap Faces',  
'TLBeginningDisplay':              'icon', 
'TLBeginningIconHover':            './maya/media/tl_beg_hover.png',
'TLBeginningIconOff':              './maya/media/tl_beg_off.png',
'TLBeginningIconOn':               './maya/media/tl_beg_on.png',
'TLBeginningInfoText':             'TIMELINE START:\nMove the timeline handle to the first frame.',
'TLBeginningState':                 False,
'TLLeftDisplay':                    'icon',   
'TLLeftIconHover':                  './maya/media/tl_left_hover.png',
'TLLeftIconOff':                    './maya/media/tl_left_off.png',
'TLLeftIconOn':                     './maya/media/tl_left_on.png',
'TLLeftInfoText':                   'TIMELEFT NUDGE LEFT:\nMove the timeline handle to the left 30 frames.',
'TLLeftState':                      False,
'TLRightDisplay':                   'icon',   
'TLRightIconHover':                 './maya/media/tl_right_hover.png',    
'TLRightIconOff':                   './maya/media/tl_right_off.png',
'TLRightIconOn':                    './maya/media/tl_right_on.png',
'TLRightInfoText':                  'TIMELEFT NUDGE RIGHT:\nMove the timeline handle to the RIGHT 30 frames.',
'TLRightState':                     False,

'SaveImageButtonDisplay':                   'text',   
'SaveImageButtonInfoText':                  'SAVE IMAGE:\nSaves the current image to your Output Folder.',
'SaveImageButtonState':                     False,
'SaveImageButtonText':             'Save Image',

'AutoSwapButtonDisplay':                   'text',   
'AutoSwapButtonInfoText':                  'AUTOSWAP:\nAutomatcially applies your currently selected Input Face to new images.',
'AutoSwapButtonState':                     False,
'AutoSwapButtonText':             'Auto Swap',
 
'ClearVramButtonDisplay':                   'text',   
'ClearVramButtonInfoText':                  'CLEAR VRAM:\nClears models from your VRAM.',
'ClearVramButtonState':                     False,
'ClearVramButtonText':             'Clear VRAM',

'GetNewEmbButtonDisplay':                   'text',
'GetNewEmbButtonInfoText':                  'CLEAR VRAM:\nClears models from your VRAM.',
'GetNewEmbButtonState':                     False,
'GetNewEmbButtonText':             'Clear VRAM',


'StopMarkerButtonnDisplay':                   'icon',
'StopMarkerButtonIconHover':            './maya/media/previous_marker_hover.png',
'StopMarkerButtonIconOff':              './maya/media/previous_marker_off.png',
'StopMarkerButtonIconOn':               './maya/media/previous_marker_off.png',
'StopMarkerButtonInfoText':                  'CLEAR VRAM:\nClears models from your VRAM.',
'StopMarkerButtonState':                     False,
'StopMarkerButtonText':             'Clear VRAM',
 
#Switches       
'ColorSwitchInfoText':              'RGB ADJUSTMENT:\nFine-tune the RGB color values of the swap.',
'ColorSwitchState':                 False,
'DiffSwitchInfoText':               'DIFFERENCER:\nAllow some of the original face to show in the swapped result when the difference between the two images is small. Can help bring back some texture to the swapped face',
'DiffSwitchState':                  False,
'FaceAdjSwitchInfoText':            'KPS and SCALE ADJUSTMENT:\nThis is an experimental feature to perform direct adjustments to the face landmarks found by the detector. There is also an option to adjust the scale of the swapped face.',
'FaceAdjSwitchState':               False,
'FaceParserSwitchInfoText':         'BACKGROUND MASK:\nAllow the unprocessed background from the orginal image to show in the final swap.',
'FaceParserSwitchState':            False,
'MouthParserSwitchInfoText':        'MOUTH MASK:\nAllow the mouth from the original face to show on the swapped face.',
'MouthParserSwitchState':           False,
'OccluderSwitchInfoText':           'OCCLUSION MASK:\nAllow objects occluding the face to show up in the swapped image.',
'OccluderSwitchState':              False,
'OrientSwitchInfoText':             'ORIENTATION:\nRotate the face detector to better detect faces at different angles',
'OrientSwitchState':                False,
'RestorerSwitchInfoText':           'FACE RESTORER:\nRestore the swapped image by upscaling.',
'RestorerSwitchState':              False,
'StrengthSwitchInfoText':           'SWAPPER STRENGTH:\nApply additional swapping iterations to increase the strength of the result, which may increase likeness',
'StrengthSwitchState':              False,
'CLIPSwitchInfoText':               'TEXT MASKING:\nUse descriptions to identify objects that will be present in the final swapped image.',
'CLIPSwitchState':                  False,

# Sliders
'BlendSliderAmount':                5,
'BlendSliderInc':                   1,  
'BlendSliderInfoText':              'BLEND:\nCombined masks blending distance. Is not applied to the border masks.',
'BlendSliderMax':                   100,
'BlendSliderMin':                   0,
'BorderBlurSliderAmount':           10,
'BorderBlurSliderInc':              1,  
'BorderBlurSliderInfoText':         'BORDER MASK BLEND:\nBorder mask blending distance.',
'BorderBlurSliderMax':              64,
'BorderBlurSliderMin':              0,
'BorderBottomSliderAmount':         10, 
'BorderBottomSliderInc':            1,  
'BorderBottomSliderInfoText':       'BOTTOM BORDER DISTANCE:\nA rectangle with adjustable top, bottom, and sides that blends the swapped face rseult back into the original image.',
'BorderBottomSliderMax':            64,
'BorderBottomSliderMin':            0,
'BorderSidesSliderAmount':          10, 
'BorderSidesSliderInc':             1,  
'BorderSidesSliderInfoText':        'SIDES BORDER DISTANCE:\nA rectangle with adjustable top, bottom, and sides that blends the swapped face result back into the original image.',
'BorderSidesSliderMax':             64,
'BorderSidesSliderMin':             0,
'BorderTopSliderAmount':            10, 
'BorderTopSliderInc':               1, 
'BorderTopSliderInfoText':          'TOP BORDER DISTANCE:\nA rectangle with adjustable top, bottom, and sides that blends the swapped face result back into the original image.',
'BorderTopSliderMax':               64,
'BorderTopSliderMin':               0,
'ColorBlueSliderAmount':            0,
'ColorBlueSliderInc':               1,  
'ColorBlueSliderInfoText':          'RGB BLUE ADJUSTMENT',
'ColorBlueSliderMax':               100,
'ColorBlueSliderMin':               -100,
'ColorGreenSliderAmount':           0,
'ColorGreenSliderInc':              1, 
'ColorGreenSliderInfoText':         'RGB GREEN ADJUSTMENT',
'ColorGreenSliderMax':              100,
'ColorGreenSliderMin':              -100,
'ColorRedSliderAmount':             0,
'ColorRedSliderInc':                1,  
'ColorRedSliderInfoText':           'RGB RED ADJUSTMENT',
'ColorRedSliderMax':                100,
'ColorRedSliderMin':                -100,
'DetectScoreSliderAmount':          50,
'DetectScoreSliderInc':             1,      
'DetectScoreSliderInfoText':        'DETECTION SCORE LIMIT:\nDetermines the minimum score required for a face to be detected. Higher values require higher quality faces. E.g., if faces are flickering when at extreme angles, raising this will limit swapping attempts.',
'DetectScoreSliderMax':             100,
'DetectScoreSliderMin':             1,
'DiffSliderAmount':                 4,   
'DiffSliderInc':                    1,
'DiffSliderInfoText':               'DIFFERENCING AMOUNT:\nHigher values relaxes the similarity constraint.',
'DiffSliderMax':                    100,
'DiffSliderMin':                    0,
'FaceParserSliderAmount':           0,   
'FaceParserSliderInc':              1,        
'FaceParserSliderInfoText':         'BACKGROUND MASK AMOUNT:\nNegative/Positive values shrink and grow the mask.',
'FaceParserSliderMax':              50,
'FaceParserSliderMin':              -50,
'FaceScaleSliderAmount':            0,
'FaceScaleSliderInc':               1,    
'FaceScaleSliderInfoText':          'FACE SCALE AMOUNT',
'FaceScaleSliderMax':               20,
'FaceScaleSliderMin':               -20,
'KPSScaleSliderAmount':             0, 
'KPSScaleSliderInc':                1,  
'KPSScaleSliderInfoText':           'KPS SCALE AMOUNT:\nGrows and shrinks the detection point distances.',
'KPSScaleSliderMax':                100,
'KPSScaleSliderMin':                -100,
'KPSXSliderAmount':                 0, 
'KPSXSliderInc':                    1,      
'KPSXSliderInfoText':               'KPS X-DIRECTION AMOUNT:\nShifts the detection points left and right',
'KPSXSliderMax':                    100,
'KPSXSliderMin':                    -100,
'KPSYSliderAmount':                 0, 
'KPSYSliderInc':                    1,  
'KPSYSliderInfoText':               'KPS Y-DIRECTION AMOUNT:\nShifts the detection points lup and down',
'KPSYSliderMax':                    100,
'KPSYSliderMin':                    -100,
'MouthParserSliderAmount':          0, 
'MouthParserSliderInc':             1,      
'MouthParserSliderInfoText':        'MOUTH MASK AMOUNT:\nAdjust the size of the mask. Negative values only mask the inside of the mouth, including the tongue. Positive values also include lips',
'MouthParserSliderMax':             50,
'MouthParserSliderMin':             -50,
'OccluderSliderAmount':             0,
'OccluderSliderInc':                1,
'OccluderSliderInfoText':           'OCCLUDER AMOUNT:\nGrows or shrinks the occluded region',
'OccluderSliderMax':                100,
'OccluderSliderMin':                -100,
'OrientSliderAmount':               0,
'OrientSliderInc':                  90,
'OrientSliderInfoText':             'ORIENTATION ANGLE:\nSet this to the angle of the input face angle to help with laying down/upside down/etc. Angles are read clockwise.',
'OrientSliderMax':                  270,
'OrientSliderMin':                  0,
'RestorerSliderAmount':             100,
'RestorerSliderInc':                5,
'RestorerSliderInfoText':           'RESTORER AMOUNT:\nBlends the Restored results back into the original swap.',
'RestorerSliderMax':                100,
'RestorerSliderMin':                0,
'StrengthSliderAmount':             100,
'StrengthSliderInc':                25,    
'StrengthSliderInfoText':           'STRENGTH AMOUNT:\nIncrease up to 5x additional swaps (500%). 200% is generally a good result. Set to 0 to turn off swapping but allow the rest of the pipeline to apply to the original image.',
'StrengthSliderMax':                500,
'StrengthSliderMin':                0,
'ThreadsSliderAmount':              5,
'ThreadsSliderInc':                 1,    
'ThreadsSliderInfoText':            'EXECUTION THREADS:\nSet number of execution threads while playing and recording. Depends strongly on GPU VRAM. 5 threads for 24GB.',
'ThreadsSliderMax':                 20,
'ThreadsSliderMin':                 1,
'ThresholdSliderAmount':            55,
'ThresholdSliderInc':               1,
'ThresholdSliderInfoText':          'THRESHHOLD AMOUNT:\nRaise to reduce faces hopping around when swapping multiple people. A higher value is stricter.',
'ThresholdSliderMax':               100,
'ThresholdSliderMin':               0,
'VideoQualSliderAmount':            18,
'VideoQualSliderInc':               1,      
'VideoQualSliderInfoText':          'VIDEO QUALITY:\nThe encoding quality of the recorded video. 0 is best, 50 is worst, 18 is mostly lossless. File size increases with a lower quality number.',
'VideoQualSliderMax':               50,
'VideoQualSliderMin':               0,

'CLIPSliderAmount':                 50,
'CLIPSliderInc':                    1,
'CLIPSliderInfoText':               'TEXT MASKING STENGTH:\nIncrease to strengthen the effect.',
'CLIPSliderMax':                    100,
'CLIPSliderMin':                    0,

'ColorGammaSliderAmount':                 1,
'ColorGammaSliderInc':                    0.02,
'ColorGammaSliderInfoText':               'GAMMA VALUE:\nChanges Gamma.',
'ColorGammaSliderMax':                    2,
'ColorGammaSliderMin':                    0,


# Text Selection
'DetectTypeTextSelInfoText':        'FACE DETECTION MODEL:\nSelect the face detection model. Mostly only subtle differences, but can significant differences when the face is at extreme angles or covered.',
'DetectTypeTextSelMode':            'Retinaface',
'DetectTypeTextSelModes':           ['Retinaface', 'Yolov8', 'SCRDF'],
'PreviewModeTextSelInfoText':       '',
'PreviewModeTextSelMode':           'Video',
'PreviewModeTextSelModes':          ['Video', 'Image','Theater'],
'RecordTypeTextSelInfoText':        'VIDEO RECORDING LIBRARY:\nSelect the recording library used for video recording. FFMPEG uses the Video Quality slider to adjust the size and quality of the final video. OPENCV has no options but is faster and produces good results.',
'RecordTypeTextSelMode':            'FFMPEG',
'RecordTypeTextSelModes':           ['FFMPEG', 'OPENCV'],
'RestorerDetTypeTextSelInfoText':   'ALIGNMENT:\nSelect how the face is aligned for the Restorer. Original preserves facial features and expressions, but can show some artifacts. Reference softens features. Blend is closer to Reference but is much faster.',
'RestorerDetTypeTextSelMode':       'Blend',
'RestorerDetTypeTextSelModes':      ['Original', 'Blend', 'Reference'],  
'RestorerTypeTextSelInfoText':      'RESTORER TYPE:\nSelect the Restorer type.\nSpeed: GPEN256>GFPGAN>CF>GPEN512',
'RestorerTypeTextSelMode':          'GFPGAN',
'RestorerTypeTextSelModes':         ['GFPGAN', 'CF', 'GPEN256', 'GPEN512'],
'MergeTextSelInfoText':      'INPUT FACES MERGE MATH:\nWhen shift-clicking face for merging, determines how the embedding vectors are combined.',
'MergeTextSelMode':          'Mean',
'MergeTextSelModes':         ['Mean', 'Median'],
'SwapperTypeTextSelInfoText':      'SWAPPER OUTPUT RESOLUTION:\nDetermines the resolution of the swapper output.',
'SwapperTypeTextSelMode':          '128',
'SwapperTypeTextSelModes':         ['128', '256', '512'],



# Text Entry
'CLIPTextEntry':    '',
'CLIPTextEntryInfoText':            'TEXT MASKING ENTRY:\nTo use, type a word(s) in the box separated by commas and press <enter>.',
}

PARAM_VARS =    {

    'CLIPState':                False,
    'CLIPMode':                 0, 
    'CLIPModes':                ['CLIP'], 
    'CLIPAmount':               [50],
    'CLIPMin':                  0,
    'CLIPMax':                  100,
    'CLIPInc':                  1,                                                  
    'CLIPUnit':                 '%', 
    'CLIPIcon':                 './maya/media/CLIP.png',
    'CLIPMessage':              'CLIP - Text based occluder. Occluded objects are visible in the final image (occluded from the mask). [LB: on/off, MW: strength]',                              
    'CLIPFunction':         False,

    "CLIPText":                 '',
}   
 
PARAMS =   { 
   
    'ClearmemFunction':         'self.clear_mem()',
    'PerfTestFunction':         'self.toggle_perf_test()',
    'ImgVidFunction':         'self.toggle_vid_img()',
    'AutoSwapFunction':         'self.toggle_auto_swap()',
    'SaveImageFunction':         'self.save_image()',

    'ClearmemIcon':            './maya/media/clear_mem.png',
    'SaveImageIcon':            './maya/media/save_disk.png', 
    'PerfTestIcon':            './maya/media/test.png',
    'RefDelIcon':          './maya/media/construction.png',
    'TransformIcon':          './maya/media/scale.png',    
    'ThresholdIcon':            './maya/media/thresh.png',
    'LoadSFacesIcon':            './maya/media/save.png',
    'BorderIcon':                 './maya/media/maskup.png',
    'OccluderIcon':             './maya/media/occluder.png',
    'ColorIcon':            './maya/media/rgb.png',
    'StrengthIcon':             './maya/media/strength.png',
    'OrientationIcon':          './maya/media/orient.png',
    'DiffIcon':                 './maya/media/diff.png',
    'MouthParserIcon':           './maya/media/parse.png',
    'AudioIcon':            './maya/media/rgb.png',    
    'VideoQualityIcon':            './maya/media/tarface.png',    
    'MaskViewIcon':             './maya/media/maskblur.png',
    'BlurIcon':                 './maya/media/blur.png',    
    'ToggleStopIcon':            './maya/media/STOP.png',    
     'DelEmbedIcon':            './maya/media/delemb.png',   
    'ImgVidIcon':            './maya/media/imgvid.png',    
    
    
    
    'ImgVidMessage':         'IMAGE/VIDEO - Toggle between Image and Video folder view.',      
    'ToggleStopMessage':         'STOP MARKER - Sets a frame that will stop the video playing/recording.',      
    'AutoSwapMessage':         'AUTO SWAP - Automatically swaps the first person in an image to the selcted source faces [LB: Turn on/off]',      
    'SaveImageMessage':         'SAVE IMAGE - Save image to output folder',      
    'ClearmemMessage':         'CLEAR VRAM - Clears all models from VRAM [LB: Clear]',      
    'PerfTestMessage':         'PERFORMANCE DATA - Displays timing data in the console for critical Rope functions. [LB: on/off]',
    'RefDelMessage':       'REFERENCE DELTA - Modify the reference points. Turn on mask preview to see adjustments. [LB: on/off, RB: translate x/y, and scale, MW: amount]' ,
    'ThresholdMessage':         'THRESHOLD - Threshold for determining if Target Faces match faces in a frame. Lower is stricter. [LB: use amount/match all, MW: value]',
    'TransformMessage':       'SCALE - Adjust the scale of the face. Use with Background parser to blend into the image. [LB: on/off, MW: amount]',     
    'PlayMessage':         'PLAY - Plays the video. Press again to stop playing',  
 
     }   
     
