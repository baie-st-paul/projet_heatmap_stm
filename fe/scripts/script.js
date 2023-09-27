


async function initMap() {
    let time = "8:00:00"
    const response = await fetch("http://127.0.0.1:5000/time/" + time)
        .then((response) =>response.json())
        .then((responseJSON) => {return  responseJSON})
        .catch(err => console.log(err));

    console.log(response);
    let heatmapArray = [];

    for (let coord of response) {

        let newHeatmapData = {
            location: new google.maps.LatLng(coord.latitude, coord.longitude),weight: coord.intensity_factor
        }
        console.log(coord)
        heatmapArray.push(newHeatmapData);
    }

    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 45.508888, lng: -73.561668},
        zoom: 12,
        mapId: "satellite"
    });
    console.log(heatmapArray[1]);


    var heatmap = new google.maps.visualization.HeatmapLayer({
        data: heatmapArray,
        map: map
    });
}


