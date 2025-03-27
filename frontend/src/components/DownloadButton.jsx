import React from "react";

const DownloadButton = ({ handleDownload, loading }) => {
  return (
    <button
      onClick={handleDownload}
      className="mt-4 px-6 py-3 bg-[#7ed214] text-white rounded-lg hover:bg-[#74ae2d] transition-all duration-300 shadow-md hover:shadow-xl flex items-center font-bold"
      disabled={loading}
    >
      {loading ? (
        <>
          <svg
            className="animate-spin h-5 w-5 mr-2 text-white font-extrabold text-3xl"
            viewBox="0 0 24 24"
          >
            <circle
              className="opacity-25"
              cx="12"
              cy="12"
              r="10"
              stroke="currentColor"
              strokeWidth="4"
            ></circle>
            <path
              className="opacity-75"
              fill="currentColor"
              d="M4 12a8 8 0 018-8v4l3-3-3-3v4a8 8 0 100 16v-4l-3 3 3 3v-4a8 8 0 01-8-8z"
            ></path>
          </svg>
          Wait...
        </>
      ) : (
        "Download Reel"
      )}
    </button>
  );
};

export default DownloadButton;
