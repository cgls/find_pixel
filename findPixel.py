###########################################################
## findIndex
# Find the HV tile number and row, column index for a given plate
# carree location for 1km Copernicus Global Land products
# 
# @author Bruno Smets, VITO NV, Belgium
#
# @attention: no error handling performed, assume correct lon, lat value
#
# @param  lon  (float)    Longitude position
# @param  lat  (float)    Latitude position
# @param  reso (int)     Resolution 1 = 112 pixels/degree (1km), 
#                                  3 = 3 * 112 pixels / degree (333m)
#
# @return   xtile  Number representing Horizontal 10° tile index
# @return   ytile  Number representing Vertical 10° tile index
# @return   idx    Row number in 10° tile (count starts from zero)
# @return   idy    Column number in 10° tile (count starts from zero)
#
def findIndex(lon, lat, reso):
        PIXRES = 112.0*reso
        HALFPIX = PIXRES*2.
        if reso == 1:
            TOP = 90.0
            NBPIX = 1121
        elif reso == 3:
            TOP = 75.0
            NBPIX = 3360
        else:
            print 'Unsupported resolution, only 1 (1km) or 3 (333m)'
            return -1, -1, -1, -1
    
        TOPY=TOP+1./HALFPIX    
        TOPX=-180-1./HALFPIX  
        #Arrays of pixel TL corner coordinates of first pixel, for each tile
        tileXStart=[-180+(i*10)-(1./HALFPIX) for i in range(37)]    #or tileXStart=numpy.arange(-180,180,10)-1/224.0
        tileYStart=[TOP-(i*10)+(1./HALFPIX) for i in range(19)]
       
        #Tile number, 0-based
        Xtile= (int((lon-TOPX)/10))
        Ytile= (int( (TOPY - lat)/10))
 
        #correct wrap around, do not favor pixel 1121 if 1km
        if Xtile == 36:
            Xtile = 00
            lon = -180.
        if Ytile == 18:
            Ytile = 00
            lat = 90.
 
        #Pixel index (count), also 0-based
        
        Xidx=int((lon-tileXStart[Xtile])*PIXRES)
        Yidx=int((tileYStart[Ytile]-lat)*PIXRES)
 
        return (Xtile, Ytile, Xidx, Yidx)
