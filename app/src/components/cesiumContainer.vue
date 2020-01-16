<template>
  <div id="cesiumContainer">
  </div>
</template>

<script>
import 'cesium/Widgets/widgets.css';
let Cesium = require('cesium/Cesium');

export default {
  name: 'cesiumContainer',
  mounted () {
    let viewer = new Cesium.Viewer('cesiumContainer', {
      animation:false,
      timeline:false,
      geocoder:false,
      baseLayerPicker:false,
      homeButton:false,
      terrainProvider : Cesium.createWorldTerrain({
        //requestWaterMask: true,
        requestVertexNormals: true
      }),
      navigationInstructionsInitiallyVisible:false,
      navigationHelpButton:false,
      selectionIndicator:false,
      fullscreenButton:false,
      requestWaterMask: true
    });

    // new Cesium.CesiumTerrainProvider({
    //   url: 'https://assets.agi.com/stk-terrain/world',
    //   requestWaterMask: true
    // });

    viewer.scene.globe.depthTestAgainstTerrain = true;
    viewer.scene.debugShowFramesPerSecond = true;

    // viewer.scene.globe.enableLighting = true;

    https://www.cnblogs.com/LXGISer/p/8427953.html
    viewer.imageryLayers.addImageryProvider(
      new Cesium.UrlTemplateImageryProvider({
        url: 'http://mt0.google.cn/vt/lyrs=s&hl=zh-CN&x={x}&y={y}&z={z}', // http://www.google.cn/maps/vt?lyrs=s@800&x={x}&y={y}&z={z}
        tilingScheme:new Cesium.WebMercatorTilingScheme(),
        minimumLevel:1,
        maximumLevel:20
      })
    );

    // viewer.imageryLayers.addImageryProvider(
    //   new Cesium.UrlTemplateImageryProvider({
    //     url:'http://www.google.cn/maps/vt?lyrs=h@189&gl=cn&x={x}&y={y}&z={z}',
    //     tilingScheme:new Cesium.WebMercatorTilingScheme(),
    //     minimumLevel:1,
    //     maximumLevel:20
    //   })
    // );

    // viewer.imageryLayers.addImageryProvider(
    //   new Cesium.WebMapTileServiceImageryProvider({
    //     url: "http://t0.tianditu.gov.cn/img_w/wmts?tk=9ed81ab8e2272c54db50b065e746f138",
    //     layer: 'img',
    //     style: 'default',
    //     tileMatrixSetID: 'w',
    //     format: 'tiles',
    //     maximumLevel: 18
    //   })
    // )

    viewer.imageryLayers.addImageryProvider(
      new Cesium.WebMapTileServiceImageryProvider({
        url: "http://t0.tianditu.gov.cn/cia_w/wmts?tk=9ed81ab8e2272c54db50b065e746f138",
        layer: 'cia',
        style: 'default',
        tileMatrixSetID: 'w',
        format: 'tiles',
        maximumLevel: 18
      })
    )

    // viewer.imageryLayers.addImageryProvider(
    //   new Cesium.WebMapServiceImageryProvider({
    //     url: 'http://localhost:8085/geoserver/test/wms',
    //     layers: 'test:tianjin_planet_osm_line_lines',//'test:tianjin_planet_osm_polygon_polygons',
    //     parameters: {
    //       service : 'WMS',
    //       format: 'image/png',
    //       transparent: true
    //     }
    //   })
    // );

    viewer.imageryLayers.addImageryProvider(
      new Cesium.WebMapServiceImageryProvider({
        url: 'http://zeit.org.cn:4096/geoserver/test/wms',
        layers: 'test:test',
        parameters: {
          service : 'WMS',
          format: 'image/png',
          transparent: true
        }
      })
    );

    viewer.imageryLayers.addImageryProvider(
      new Cesium.WebMapServiceImageryProvider({
        url: 'http://zeit.org.cn:4096/geoserver/sf/wms',
        layers: 'sf:streams',
        parameters: {
          service : 'WMS',
          format: 'image/png',
          transparent: true
        }
      })
    );

    var tileset = viewer.scene.primitives.add(new Cesium.Cesium3DTileset({
      url: 'http://localhost:8080/static/data/3dtiles5/tileset.json',
      //maximumScreenSpaceError: 2,
      //maximumNumberOfLoadedTiles: 100,
    }));
    viewer.zoomTo(tileset);
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>

<style>
.cesium-widget-credits {
 display: none!important;
 visibility: hidden!important;
}
</style>
