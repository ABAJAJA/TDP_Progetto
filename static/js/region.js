const URL = "/api/v1/getcitypollution";
const header = { "X-Api-Token": "SJPTjZSxUWGGTUTGVUDoteNOPNRCdHsS" };

document
  .getElementById("region-select")
  .addEventListener("change", function () {
    const region = this.value;

    fetch(URL, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        ...header,
      },
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("Errore nella richiesta: " + response.statusText);
        }
        return response.json();
      })
      .then((data) => {
        document.getElementById("pm10").textContent = data.pm10;
        document.getElementById("pm2_5").textContent = data.pm2_5;
        document.getElementById("no2").textContent = data.NO2;
      })
      .catch((error) => console.error("Errore nella richiesta:", error));
  });
