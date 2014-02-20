# Spec file auto generated on 2014-02-19 by user root from script gen-rpmspec

%define pkgname       ruby
%define pkgver        1.9.3
%define pkgverrel     448
%define ruby          %{pkgname}-%{pkgver}-p%{pkgverrel}
%define installroot   opt
%define installdir    %{installroot}/%{ruby}
##%define passengermod  mod_passenger.so
%define apachemoddir  etc/httpd/modules

Name:             %{pkgname}
Version:          %{pkgver}.%{pkgverrel}
Release:          1%{?dist}
Summary:          Installer package for %{ruby}
Group:            Development/Languages
License:          Ruby License/GPL
URL:              http://ftp.ruby-lang.org/pub/ruby/1.9.3
Source0:          %{ruby}-environment.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{pkgverrel}-%{release}-root-%(%{__id_u} -n)
Packager:         Cody Lane <cody.lane@gmail.com.com>
Requires:         httpd
Provides:         ruby = %{pkgver}
Provides:         /opt/ruby-1.9.3-p448/lib/libruby.so.1.9()
Provides:         /opt/ruby-1.9.3-p448/lib/libruby.so.1.9.1()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/racc/cparse.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/dl/callback.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/sdbm.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/readline.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/date_core.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/syslog.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/openssl.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/continuation.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/strscan.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/pty.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/fiber.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/stringio.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/dbm.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/mathn/complex.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/mathn/rational.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/etc.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/fcntl.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/fiddle.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/objspace.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/pathname.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/socket.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/psych.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/iconv.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/coverage.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/json/ext/generator.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/json/ext/parser.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/digest.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/nkf.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/utf_16be.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/iso_8859_1.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/trans/emoji_iso2022_kddi.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/trans/japanese_sjis.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/trans/big5.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/trans/iso2022.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/trans/korean.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/trans/gb18030.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/trans/emoji_sjis_kddi.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/trans/transdb.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/trans/utf8_mac.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/trans/utf_16_32.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/trans/single_byte.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/trans/japanese.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/trans/emoji_sjis_softbank.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/trans/emoji.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/trans/chinese.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/trans/japanese_euc.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/trans/emoji_sjis_docomo.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/trans/escape.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/trans/gbk.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/iso_8859_6.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/big5.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/iso_8859_16.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/utf_16le.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/koi8_r.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/gb18030.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/iso_8859_7.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/windows_1251.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/euc_kr.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/iso_8859_3.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/iso_8859_15.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/encdb.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/iso_8859_13.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/euc_jp.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/iso_8859_9.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/iso_8859_11.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/koi8_u.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/euc_tw.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/iso_8859_4.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/iso_8859_10.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/utf_32le.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/iso_8859_14.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/iso_8859_8.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/emacs_mule.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/shift_jis.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/gb2312.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/utf_32be.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/iso_8859_5.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/iso_8859_2.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/cp949.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/enc/gbk.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/syck.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/zlib.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/gdbm.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/dl.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/curses.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/digest/rmd160.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/digest/bubblebabble.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/digest/sha1.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/digest/md5.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/digest/sha2.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/bigdecimal.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/ripper.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/io/nonblock.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/io/wait.so()
Provides:         /opt/ruby-1.9.3-p448/lib/ruby/1.9.1/x86_64-linux/io/console.so()
Provides:         /opt/ruby-1.9.3-p448/lib/libruby.so()
Provides:         bigdecimal = 1.1.0
Provides:         io-console = 0.3
Provides:         json = 1.5.5
Provides:         minitest = 2.5.1
Provides:         rake = 0.9.2.2
Provides:         rdoc = 3.9.5
AutoReqProv:      no
Requires(post):   findutils

%description
Ruby is the interpreted scripting language for quick and easy
object-oriented programming.  It has many features to process text
files and to do system management tasks (as in Perl).  It is simple,
straight-forward, and extensible.

%prep
rm -fr %{ruby}
mkdir -p %{ruby}
cd %{ruby}
tar zxvf %{SOURCE0}

%install
rm -fr %{buildroot}
mkdir -p %{buildroot}
cp -ra %{ruby}/%{installroot} %{buildroot}

%clean
rm -fr %{buildroot}

%post
##PASSENGER_MOD=$(find /%{installroot} -iname "%{passengermod}" -type f)
##[ -n "$PASSENGER_MOD" ] && cp "$PASSENGER_MOD" /%{apachemoddir}/
cd /%{installroot}
[ -L 'ruby' ] && unlink ruby
ln -sf %{ruby} ruby

%postun
##rm -f /%{apachemoddir}/%{passengermod}
rm -fr %{installdir}

%files
%defattr(-,root,root,-)
/%{installdir}

%changelog
