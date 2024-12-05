
        // Texto para Áudio
        document.getElementById('textToAudioForm').addEventListener('submit', async (event) => {
          event.preventDefault();
          const text = document.getElementById('text').value;

          const response = await fetch('http://127.0.0.1:8001/api/text-to-audio/', {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({ text: text })
          });

          if (response.ok) {
              const blob = await response.blob();
              const audioPlayer = document.getElementById('audioPlayer');
              audioPlayer.src = URL.createObjectURL(blob);
              audioPlayer.style.display = 'block';
          } else {
              alert('Erro ao converter texto para áudio.');
          }
      });

      // Áudio para Texto
      document.getElementById('audioToTextForm').addEventListener('submit', async (event) => {
          event.preventDefault();
          const formData = new FormData();
          formData.append('audio', document.getElementById('audioFile').files[0]);
          formData.append('language','pt');

          const response = await fetch('http://127.0.0.1:8000/api/transcribe/', {
              method: 'POST',
              body: formData
          });

          if (response.ok) {
              const data = await response.json();
              console.log(data)
              const transcribedText = document.getElementById('transcribedText');
              transcribedText.querySelector('p').textContent = data.transcription;
              transcribedText.style.display = 'block';
          } else {
              alert('Erro ao transcrever áudio.');
          }
      });

      // // Download de Vídeos
      // document.getElementById('youtubeDownloadForm').addEventListener('submit', async (event) => {
      //     event.preventDefault();
      //     const youtubeLink = document.getElementById('youtubeLink').value;
      //     const format = document.getElementById('format').value;

      //     const response = await fetch('http://127.0.0.1:8002/api/youtube-download/', {
      //         method: 'POST',
      //         headers: { 'Content-Type': 'application/json' },
      //         body: JSON.stringify({ url: youtubeLink, format: format })
      //     });

      //     if (response.ok) {
      //         const blob = await response.blob();
      //         const link = document.createElement('a');
      //         link.href = URL.createObjectURL(blob);
      //         link.download = `youtube.${format === 'audio' ? 'mp3' : 'mp4'}`;
      //         link.click();
      //     } else {
      //         alert('Erro ao baixar vídeo.');
      //     }
      // });
