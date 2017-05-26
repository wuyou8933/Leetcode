from qgis.core import QGis, QgsFeatureRequest, QgsFeature, QgsGeometry, QgsWKBTypes
myDir = '/Users/jouanchen/Desktop/Myanmar/'
for vLayer in iface.mapCanvas().layers():
    QgsVectorFileWriter.writeAsVectorFormat(vLayer,
    myDir + vLayer.name() + ".csv", 'utf-8',
    vLayer.crs(), "CSV",layerOptions =['GEOMETRY=AS_WKT'])


for vLayer in iface.mapCanvas().layers():
    print vLayer
    import pdb;pdb.set_trace()


for vLayer in iface.mapCanvas().layers():
	QgsVectorFileWriter.writeAsVectorFormat('vLayer,
	myDir + vLayer.name() + ".csv", 'utf-8',vLayer.crs(), "CSV",layerOptions =['GEOMETRY=AS_WKT'],geom_type=ogr.wkbPoint25D)
