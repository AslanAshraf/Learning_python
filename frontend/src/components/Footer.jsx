// components/Footer.jsx
import { FaInstagram, FaTwitter, FaFacebook, FaQuestionCircle, FaPhone, FaEnvelope } from 'react-icons/fa';

const Footer = () => {
  return (
    <footer className="bg-gradient-to-r from-purple-800 to-pink-800 text-white mt-20">
      <div className="max-w-7xl mx-auto py-12 px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">

          {/* Brand Info */}
          <div className="space-y-4">
            <div className="flex items-center">
              <FaInstagram className="h-8 w-8 text-white" />
              <span className="ml-2 text-xl font-bold">
                Reel<span className="text-yellow-300">Downloader</span>
              </span>
            </div>
            <p className="text-purple-100">
              The fastest way to download Instagram Reels without watermark in HD quality.
            </p>
            <div className="flex space-x-4">
              <a href="#" className="text-purple-200 hover:text-white transition-colors">
                <FaInstagram className="h-5 w-5" />
              </a>
              <a href="#" className="text-purple-200 hover:text-white transition-colors">
                <FaTwitter className="h-5 w-5" />
              </a>
              <a href="#" className="text-purple-200 hover:text-white transition-colors">
                <FaFacebook className="h-5 w-5" />
              </a>
            </div>
          </div>

          {/* Quick Links */}
          <div>
            <h3 className="text-lg font-semibold mb-4">Quick Links</h3>
            <ul className="space-y-2">
              <li><a href="#" className="text-purple-200 hover:text-white transition-colors">Features</a></li>
              <li><a href="https://www.loom.com/share/601a799697b047fdb1a146638e8b97a9" target='_blank' className="text-purple-200 hover:text-white transition-colors">How It Works</a></li>
              <li><a href="#" className="text-purple-200 hover:text-white transition-colors">FAQ</a></li>
            </ul>
          </div>

          {/* Legal */}
          <div>
            <h3 className="text-lg font-semibold mb-4">Legal</h3>
            <ul className="space-y-2">
              <li><a href="#" className="text-purple-200 hover:text-white transition-colors">Privacy Policy</a></li>
              <li><a href="#" className="text-purple-200 hover:text-white transition-colors">Terms of Service</a></li>
              <li><a href="#" className="text-purple-200 hover:text-white transition-colors">Cookie Policy</a></li>
            </ul>
          </div>

          {/* Contact */}
          <div>
            <h3 className="text-lg font-semibold mb-4">Contact Us</h3>
            <ul className="space-y-3">
              <li className="flex items-center">
                <FaEnvelope className="mr-2 text-purple-200" />
                <span>support@reeldownloader.com</span>
              </li>
              <li className="flex items-center">
                <FaPhone className="mr-2 text-purple-200" />
                <span>+1 (555) 123-4567</span>
              </li>
              <li className="flex items-center">
                <FaQuestionCircle className="mr-2 text-purple-200" />
                <span>Help Center</span>
              </li>
            </ul>
          </div>
        </div>

        {/* Copyright */}
        <div className="mt-12 pt-8 border-t border-purple-700 text-center text-purple-200">
          <p>© {new Date().getFullYear()} ReelDownloader. All rights reserved.</p>
          <p className="mt-2 text-sm">
            This service is not affiliated with, endorsed by, or associated with Instagram in any way. The trademarks, logos, and brand names mentioned belong to their respective owners. ReelDownloader does not encourage copyright infringement; users are responsible for ensuring compliance with applicable laws.</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;