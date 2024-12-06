const API_BASE_URL = "http://127.0.0.1:8000/api/services/";

const serviceDropdown = document.getElementById("service");
const audioToTextForm = document.getElementById("audio-to-text-form");
const videoDownloadForm = document.getElementById("video-download-form");
const textToAudioForm = document.getElementById("text-to-audio-form");
const resultDiv = document.getElementById("result");

// Alterna os formulários de acordo com o serviço selecionado
serviceDropdown.addEventListener("change", () => {
  const selectedService = serviceDropdown.value;

  audioToTextForm.classList.add("hidden");
  videoDownloadForm.classList.add("hidden");
  textToAudioForm.classList.add("hidden");

  if (selectedService === "audio_to_text") {
    audioToTextForm.classList.remove("hidden");
  } else if (selectedService === "video_download") {
    videoDownloadForm.classList.remove("hidden");
  } else if (selectedService === "text_to_audio") {
    textToAudioForm.classList.remove("hidden");
  }
});

// Envia o áudio para transcrição
function submitAudio() {
  const audioFile = document.getElementById("audio-file").files[0];
  if (!audioFile) return alert("Por favor, selecione um arquivo de áudio.");

  const formData = new FormData();
  formData.append("service_type", "audio_to_text");
  formData.append("data", audioFile);

  fetch(API_BASE_URL, {
    method: "POST",
    body: formData,
  })
    .then(response => response.json())
    .then(data => {
      displayResult(data);
    })
    .catch(error => {
      console.error("Erro:", error);
    });
}

// Envia o link do vídeo para download
function submitVideo() {
  const videoUrl = document.getElementById("video-url").value;
  const videoFormat = document.getElementById("video-format").value;

  if (!videoUrl) return alert("Por favor, insira uma URL de vídeo.");

  fetch(API_BASE_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      service_type: "video_download",
      data: { url: videoUrl, format: videoFormat },
    }),
  })
    .then(response => response.json())
    .then(data => {
      displayResult(data);
    })
    .catch(error => {
      console.error("Erro:", error);
    });
}

// Envia o texto para conversão em áudio
function submitText() {
  const textInput = document.getElementById("text-input").value;

  if (!textInput) return alert("Por favor, insira algum texto.");

  fetch(API_BASE_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      service_type: "text_to_audio",
      data: { text: textInput },
    }),
  })
    .then(response => response.json())
    .then(data => {
      displayResult(data);
    })
    .catch(error => {
      console.error("Erro:", error);
    });
}

// Exibe o resultado na tela
function displayResult(data) {
  resultDiv.innerHTML = `
    <h3>Resultado:</h3>
    <pre>${JSON.stringify(data, null, 2)}</pre>
  `;
}
