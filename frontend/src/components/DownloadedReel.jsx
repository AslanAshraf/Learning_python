import React from "react";

const DownloadedReel = ({ download, handleDirectDownload }) => {
  if (!download) return null;

  return (
    <div className="mt-6 w-full max-w-lg px-4">
      <h2 className="text-xl font-semibold mb-3 text-red-900 text-center">
        Downloaded Reel ({download.quality}p)
      </h2>
      <div className="flex flex-col sm:flex-row items-center justify-between bg-[#e8efdf] p-3 rounded-lg shadow-md">
        <div className="flex items-center mb-3 sm:mb-0">
          <img
            src={download.thumbnailUrl}
            alt="Reel thumbnail"
            className="w-20 h-20 object-cover rounded mr-10"
            onError={(e) => {
              e.target.onerror = null;
              e.target.src = defaultThumbnail;
            }}
          />
          <p className="text-blue-500 text-lg font-bold ">Click the Button 👉</p>
        </div>
        <button
          onClick={() => handleDirectDownload(download.videoUrl)}
          className="px-4 py-2 bg-[#7ed214] text-white rounded-lg hover:bg-[#74ae2d] transition-all duration-300 shadow-md hover:shadow-xl flex items-center font-bold"
        >
          Download
        </button>
      </div>
    </div>
  );
};

export default DownloadedReel;
