# Changelog

## 1.6.0

  - Feat: Add custom htdocs_path for bootset (#18)
  - Fix: disklessset check if image is mounted (#19)

## 1.5.0

  - Fix: bootset - Remove packaging from dependencies (#17)
  - Stop tool if cannot umount image (#16)
  - Fix: bluebanquise-filters - Clustershell package (#14)
  - Fix: Improve yaml loader. (#15)

## 1.0.0

  - Fix: livenet optimization breaking image builds (#7)
  - Fix: update disklessset.spec with required dependencies and paths (#5)
  - Fix livenet selinux enabled images not booting properly (#4)
  - Added kernel-modules package to the standard livenet image type (#3)
  - Update initramfs in image_data and regenerate boot.ipxe when changing kernel (#2)
  - More direct confirmation request message in disklessset menu options 3/7 (#1)
