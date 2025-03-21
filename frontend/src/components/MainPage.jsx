import { useState, useEffect } from "react";
import axios from "axios";
import InputForm from "./InputForm";
import DownloadList from "./DownloadList ";

function MainPage() {
  const [downloadUrls, setDownloadUrls] = useState(() => {
    const savedUrls = localStorage.getItem("downloadedReels");
    return savedUrls ? JSON.parse(savedUrls) : [];
  });

  useEffect(() => {
    localStorage.setItem("downloadedReels", JSON.stringify(downloadUrls));
  }, [downloadUrls]);

  const handleDownload = async (url) => {
    try {
      const response = await axios.get(`http://127.0.0.1:5000/download/`, {
        params: { url },
      });

      const newUrls = [...downloadUrls, response.data.download_url];
      setDownloadUrls(newUrls);

    } catch (error) {
      alert("Failed to fetch the video. Try again.");
    }
  };

  const handleDirectDownload = async (videoUrl) => {
    try {
      const response = await axios.get(videoUrl, {
        responseType: "blob",
      });

      const url = window.URL.createObjectURL(new Blob([response.data]));
      const a = document.createElement("a");
      a.href = url;
      a.download = "Instagram_Reel.mp4";
      document.body.appendChild(a);
      a.click();
      a.remove();
    } catch (error) {
      alert("Failed to download the video.");
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-6">
      <h1 className="text-3xl font-bold mb-6 text-blue-700">
        Instagram Reel Downloader
      </h1>

      <InputForm onDownload={handleDownload} />
      <DownloadList downloadUrls={downloadUrls} onDirectDownload={handleDirectDownload} />
    </div>
  );
}

export default MainPage;
