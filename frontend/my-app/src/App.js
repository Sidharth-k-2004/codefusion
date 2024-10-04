// import React from 'react';

// const SpotifyPlayer = () => {
//   return (
//     <div style={{ textAlign: 'center', marginTop: '20px' }}>
//       <h2>Play Your Favorite Song</h2>
//       <iframe
//         style={{ borderRadius: '12px' }}
//         src="https://open.spotify.com/embed/track/75Pos7nHiygbxinaGoEju8?utm_source=generator"
//         width="300"
//         height="380"
//         frameBorder="0"
//         allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
//       ></iframe>
//       <iframe
//         style={{ borderRadius: '12px' }}
//         src="https://open.spotify.com/track/3WKoi3sCS6sV01TksvrupI"
//         width="300"
//         height="380"
//         frameBorder="0"
//         allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
//       ></iframe>
//     </div>
//   );
// };

// export default SpotifyPlayer;

import React from 'react';

const SpotifyPlayer = () => {
  return (
    <div style={{ textAlign: 'center', marginTop: '20px' }}>
      <h2>Play Your Favorite Song</h2>

      {/* First Song Embed */}
      <iframe
        style={{ borderRadius: '12px' }}
        src="https://open.spotify.com/embed/track/75Pos7nHiygbxinaGoEju8?utm_source=generator"
        width="300"
        height="380"
        frameBorder="0"
        allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
      ></iframe>

      {/* Second Song Embed */}
      <iframe
        style={{ borderRadius: '12px', marginTop: '20px' }}
        src="https://open.spotify.com/embed/track/3WKoi3sCS6sV01TksvrupI?utm_source=generator"
        width="300"
        height="380"
        frameBorder="0"
        allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
      ></iframe>
    </div>
  );
};

export default SpotifyPlayer;
