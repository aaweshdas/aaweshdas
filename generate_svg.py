import base64
import os

def main():
    # Read the binary font file directly to prevent any base64 encoding/BOM corruption
    font_path = os.path.join('psychlone', 'Psychlone.otf')
    if not os.path.exists(font_path):
        print(f"Error: {font_path} not found.")
        return
        
    with open(font_path, 'rb') as f:
        font_data = f.read()
    
    font_base64 = base64.b64encode(font_data).decode('utf-8')

    # Construct the SVG string with the embedded uncorrupted font
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 300" width="100%" height="100%">
  <defs>
    <!-- Background Grid Pattern -->
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#161f30" stroke-width="1.5" opacity="0.6"/>
    </pattern>

    <!-- Neon Cyber Gradient -->
    <linearGradient id="cyberGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00f2fe" />
      <stop offset="50%" stop-color="#9b51e0" />
      <stop offset="100%" stop-color="#ff007f" />
    </linearGradient>

    <!-- Border Glow Filter -->
    <filter id="neonGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>

    <!-- Embed Custom Font -->
    <style>
      @font-face {{
        font-family: 'Psychlone';
        src: url('data:font/otf;base64,{font_base64}') format('opentype');
        font-weight: normal;
        font-style: normal;
      }}
      
      .title {{
        font-family: 'Psychlone', 'Segoe UI', -apple-system, sans-serif;
        font-weight: normal;
        font-size: 42px;
        fill: #ffffff;
        letter-spacing: 2px;
      }}
      .subtitle {{
        font-family: 'Fira Code', 'Courier New', monospace;
        font-weight: 700;
        font-size: 15px;
        fill: #ff007f;
        letter-spacing: 3px;
      }}
      .desc {{
        font-family: 'Segoe UI', -apple-system, sans-serif;
        font-size: 14px;
        fill: #94a3b8;
      }}
      .term-text {{
        font-family: 'Fira Code', 'Courier New', monospace;
        font-size: 12px;
      }}
      .term-label {{
        font-weight: bold;
      }}
      .cursor {{
        fill: #00f2fe;
      }}
      @keyframes blink {{
        0%, 100% {{ opacity: 1; }}
        50% {{ opacity: 0; }}
      }}
      .blink-anim {{
        animation: blink 1.2s infinite;
      }}
      @keyframes pulse {{
        0%, 100% {{ opacity: 0.8; }}
        50% {{ opacity: 0.4; }}
      }}
      .grid-bg {{
        animation: pulse 4s infinite ease-in-out;
      }}
    </style>
  </defs>

  <!-- Deep Dark Outer Space Background -->
  <rect width="100%" height="100%" fill="#0a0d16" />
  
  <!-- Glowing subtle tech grid -->
  <rect class="grid-bg" width="100%" height="100%" fill="url(#grid)" />

  <!-- Outer Glassmorphic Card Container -->
  <!-- Glowing Shadow behind the card -->
  <rect x="25" y="25" width="750" height="250" rx="16" fill="none" stroke="url(#cyberGradient)" stroke-width="2" filter="url(#neonGlow)" opacity="0.3" />
  
  <!-- Main Card Body -->
  <rect x="25" y="25" width="750" height="250" rx="16" fill="#0f1424" fill-opacity="0.9" stroke="url(#cyberGradient)" stroke-width="1.5" />

  <!-- Terminal Window Header Bar -->
  <path d="M 25 41 A 16 16 0 0 1 41 25 L 759 25 A 16 16 0 0 1 775 41 L 775 58 L 25 58 Z" fill="#171e30" />
  
  <!-- Window Controls (Red, Yellow, Green dots) -->
  <circle cx="50" cy="41" r="6" fill="#ff5f56" />
  <circle cx="70" cy="41" r="6" fill="#ffbd2e" />
  <circle cx="90" cy="41" r="6" fill="#27c93f" />
  
  <!-- Terminal Tab Info -->
  <text x="115" y="46" font-family="'Fira Code', monospace" font-size="12" fill="#64748b">aawesh@system:~</text>

  <!-- ================= LEFT PANEL: INTRO ================= -->
  <!-- Title in Psychlone Font (All Caps to match font style) -->
  <text x="55" y="115" class="title">AAWESH KR</text>
  
  <!-- Animated / Glow Subtitle -->
  <text x="55" y="148" class="subtitle">B-TECH CSE III YEAR</text>
  
  <!-- Description -->
  <text x="55" y="180" class="desc">Aspiring Software Architect &amp; AI Researcher.</text>
  <text x="55" y="202" class="desc">Engineering intelligent systems and algorithmic solutions.</text>

  <!-- Interactive Mock terminal line -->
  <text x="55" y="240" font-family="'Fira Code', monospace" font-size="13" fill="#64748b">aaweshdas.sh --status</text>
  <text x="215" y="240" font-family="'Fira Code', monospace" font-size="13" fill="#38bdf8">active</text>
  <rect class="blink-anim cursor" x="268" y="227" width="8" height="15" />

  <!-- Vertical Dashboard Divider (Shifted Left to prevent right panel overflow) -->
  <line x1="390" y1="80" x2="390" y2="245" stroke="#1e293b" stroke-width="1.5" stroke-dasharray="4 4" />

  <!-- ================= RIGHT PANEL: SYSTEM DIAGNOSTICS ================= -->
  <!-- Diagnostic Stats (Shifted Left and resized to 12px for perfect container fitting) -->
  <!-- Line 1: OS / Identity -->
  <text x="415" y="105" class="term-text" fill="#38bdf8">
    <tspan class="term-label" fill="#00f2fe">SYSTEM:</tspan> CSE Kernel v3.0 (Internship_Ready)
  </text>
  
  <!-- Line 2: Stack -->
  <text x="415" y="132" class="term-text" fill="#a855f7">
    <tspan class="term-label" fill="#9b51e0">STACK:</tspan>  C++ / Python / React / Node.js
  </text>
  
  <!-- Line 3: Main Project -->
  <text x="415" y="159" class="term-text" fill="#f43f5e">
    <tspan class="term-label" fill="#ff007f">PROJECT:</tspan> Dorothy AI (Collabs Open)
  </text>
  
  <!-- Line 4: Current Focus -->
  <text x="415" y="186" class="term-text" fill="#10b981">
    <tspan class="term-label" fill="#34d399">LEARNING:</tspan> Advanced CP &amp; Neural Nets
  </text>
  
  <!-- Line 5: Status -->
  <text x="415" y="213" class="term-text" fill="#fbbf24">
    <tspan class="term-label" fill="#fbbf24">STATUS:</tspan>  active_learning = true
  </text>

  <!-- Neofetch-style Terminal Color Blocks -->
  <g transform="translate(415, 235)">
    <rect x="0" y="0" width="16" height="12" rx="2" fill="#00f2fe" />
    <rect x="22" y="0" width="16" height="12" rx="2" fill="#9b51e0" />
    <rect x="44" y="0" width="16" height="12" rx="2" fill="#ff007f" />
    <rect x="66" y="0" width="16" height="12" rx="2" fill="#34d399" />
    <rect x="88" y="0" width="16" height="12" rx="2" fill="#fbbf24" />
    <rect x="110" y="0" width="16" height="12" rx="2" fill="#f97316" />
    <rect x="132" y="0" width="16" height="12" rx="2" fill="#64748b" />
  </g>

</svg>
"""
    
    with open('profile_banner.svg', 'w', encoding='utf-8') as f:
        f.write(svg_content)
        
    print("Successfully generated profile_banner.svg with embedded uncorrupted Psychlone font!")

if __name__ == '__main__':
    main()
