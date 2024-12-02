function resizeTextToFit(options = {}) {
  // Default options with ability to customize
  const defaultOptions = {
    minFontSize: 8,    // Minimum font size in pixels
    maxFontSize: 64,   // Maximum font size to prevent overflow
    scaleFactor: 0.95, // Slight scale down for breathing room
    debug: false       // Optional debug logging
  };

  // Merge provided options with defaults
  const settings = { ...defaultOptions, ...options };

  // Select all table cells
  const cells = document.querySelectorAll('td');

  cells.forEach(cell => {
    // Find the paragraph in the cell
    const p = cell.querySelector('p');
    
    // Skip if no paragraph found
    if (!p) return;

    // Reset styles to ensure accurate measurement
    p.style.fontSize = ''; 
    p.style.transform = 'scale(1)';
    p.style.transformOrigin = 'top left';

    // Start with the minimum font size
    let fontSize = settings.minFontSize;
    p.style.fontSize = `${fontSize}px`;

    // Precise scaling algorithm
    while (fontSize < settings.maxFontSize) {
      // Set current font size
      p.style.fontSize = `${fontSize}px`;

      // Check if text fits
      const textFits = 
        p.scrollHeight <= cell.clientHeight && 
        p.scrollWidth <= cell.clientWidth;

      // Debug logging if enabled
      if (settings.debug) {
        console.log(`Font size: ${fontSize}px`, {
          textHeight: p.scrollHeight,
          cellHeight: cell.clientHeight,
          textWidth: p.scrollWidth,
          cellWidth: cell.clientWidth,
          fits: textFits
        });
      }

      // If text fits, try next size
      if (textFits) {
        fontSize++;
      } else {
        // If text doesn't fit, use previous size
        fontSize--;
        p.style.fontSize = `${fontSize}px`;
        break;
      }
    }

    // Apply slight scale factor for breathing room
    p.style.transform = `scale(${settings.scaleFactor})`;
    p.style.transformOrigin = 'center';

    // Optional: Handle extreme cases
    if (fontSize <= settings.minFontSize) {
      p.style.overflow = 'hidden';
      p.style.textOverflow = 'ellipsis';
    }
  });
}

// Usage examples
document.addEventListener('DOMContentLoaded', () => {
  // Default usage
  resizeTextToFit();

  // Custom usage with options
  // resizeTextToFit({
  //   minFontSize: 10,
  //   maxFontSize: 48,
  //   scaleFactor: 0.98,
  //   debug: true
  // });
});

// Optional: Resize on window resize
window.addEventListener('resize', resizeTextToFit);// JavaScript Document