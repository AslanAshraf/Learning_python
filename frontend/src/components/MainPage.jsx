import React, { useState } from "react";
import axios from "axios";
import InputField from "./InputField";
import DownloadButton from "./DownloadButton";
import DownloadedReel from "./DownloadedReel";

function MainPage() {
  const [url, setUrl] = useState("");
  const [download, setDownload] = useState(null);
  const [loading, setLoading] = useState(false);
  const [selectedQuality, setSelectedQuality] = useState("720");
  const THUMBNAIL_API_URL = import.meta.env.VITE_THUMBNAIL_API_URL;
  const DOWNLOAD_API_URL = import.meta.env.VITE_DOWNLOAD_API_URL;
  console.log(THUMBNAIL_API_URL)
  const handleDownload = async () => {
    if (!url.trim()) {
      alert("Please enter a valid Instagram Reel URL.");
      return;
    }

    setLoading(true);

    try {
      const response = await axios.get(DOWNLOAD_API_URL, {
        params: { url, quality: selectedQuality },
      });

      setDownload({
        videoUrl: response.data.download_url,
        thumbnailUrl: `${THUMBNAIL_API_URL}${encodeURIComponent(response.data.thumbnail_url)}`,
        shortcode: response.data.shortcode,
        quality: selectedQuality,
      });
      setUrl("");
    } catch (error) {
      alert("Failed to fetch the video. Try again.");
      console.error(error);
    } finally {
      setLoading(false);
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
      a.download = `Instagram_Reel_${download.quality}p.mp4`;
      document.body.appendChild(a);
      a.click();
      a.remove();
    } catch (error) {
      alert("Failed to download the video.");
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-6">
      <h1 className="text-3xl md:text-4xl font-bold mb-6 text-blue-700 text-center">
        <span className="text-3xl md:text-4xl font-bold mb-6 text-red-900">
          Instagram
        </span>{" "}
        Reel Downloader
      </h1>

      <InputField url={url} setUrl={setUrl} selectedQuality={selectedQuality} setSelectedQuality={setSelectedQuality} />

      <DownloadButton handleDownload={handleDownload} loading={loading} />

      <DownloadedReel download={download} handleDirectDownload={handleDirectDownload} />
    </div>
  );
}

export default MainPage;
