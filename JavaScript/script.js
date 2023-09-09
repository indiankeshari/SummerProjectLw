const videoElement = document.getElementById('videoElement');
const startButton = document.getElementById('startButton');
const stopButton = document.getElementById('stopButton');
const downloadButton = document.getElementById('downloadButton');
let mediaRecorder;
let recordedChunks = [];
let stream;

async function startStream() {
  try {
    stream = await navigator.mediaDevices.getUserMedia({ video: true });
    videoElement.srcObject = stream;
    mediaRecorder = new MediaRecorder(stream);

    mediaRecorder.ondataavailable = (event) => {
      if (event.data.size > 0) {
        recordedChunks.push(event.data);
      }
    };

    mediaRecorder.onstop = () => {
      downloadButton.disabled = false;
    };

    mediaRecorder.start();
    startButton.disabled = true;
    stopButton.disabled = false;
  } catch (error) {
    console.error('Error accessing webcam:', error);
  }
}

function stopStream() {
  mediaRecorder.stop();
  stream.getTracks().forEach(track => track.stop());
  videoElement.srcObject = null;
  startButton.disabled = false;
  stopButton.disabled = true;
}

function downloadVideo() {
  const blob = new Blob(recordedChunks, { type: 'video/webm' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'streamed_video.webm';
  a.click();
  URL.revokeObjectURL(url);
}

startButton.addEventListener('click', startStream);
stopButton.addEventListener('click', stopStream);
downloadButton.addEventListener('click', downloadVideo);
