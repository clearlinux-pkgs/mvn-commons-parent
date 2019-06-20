#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-commons-parent
Version  : 11
Release  : 1
URL      : https://github.com/apache/commons-parent/archive/commons-parent-11.tar.gz
Source0  : https://github.com/apache/commons-parent/archive/commons-parent-11.tar.gz
Source1  : https://repo1.maven.org/maven2/org/apache/commons/commons-parent/11/commons-parent-11.pom
Source2  : https://repo1.maven.org/maven2/org/apache/commons/commons-parent/17/commons-parent-17.pom
Source3  : https://repo1.maven.org/maven2/org/apache/commons/commons-parent/22/commons-parent-22.pom
Source4  : https://repo1.maven.org/maven2/org/apache/commons/commons-parent/24/commons-parent-24.pom
Source5  : https://repo1.maven.org/maven2/org/apache/commons/commons-parent/25/commons-parent-25.pom
Source6  : https://repo1.maven.org/maven2/org/apache/commons/commons-parent/33/commons-parent-33.pom
Source7  : https://repo1.maven.org/maven2/org/apache/commons/commons-parent/34/commons-parent-34.pom
Source8  : https://repo1.maven.org/maven2/org/apache/commons/commons-parent/37/commons-parent-37.pom
Source9  : https://repo1.maven.org/maven2/org/apache/commons/commons-parent/38/commons-parent-38.pom
Source10  : https://repo1.maven.org/maven2/org/apache/commons/commons-parent/39/commons-parent-39.pom
Source11  : https://repo1.maven.org/maven2/org/apache/commons/commons-parent/41/commons-parent-41.pom
Source12  : https://repo1.maven.org/maven2/org/apache/commons/commons-parent/42/commons-parent-42.pom
Source13  : https://repo1.maven.org/maven2/org/apache/commons/commons-parent/43/commons-parent-43.pom
Source14  : https://repo1.maven.org/maven2/org/apache/commons/commons-parent/47/commons-parent-47.pom
Source15  : https://repo1.maven.org/maven2/org/apache/commons/commons-parent/5/commons-parent-5.pom
Source16  : https://repo1.maven.org/maven2/org/apache/commons/commons-parent/7/commons-parent-7.pom
Source17  : https://repo1.maven.org/maven2/org/apache/commons/commons-parent/9/commons-parent-9.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-commons-parent-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-commons-parent package.
Group: Data

%description data
data components for the mvn-commons-parent package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/11
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/11

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/17
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/17

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/22
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/22

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/24
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/24

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/25
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/25

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/33
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/33

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/34
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/34

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/37
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/37

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/38
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/38

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/39
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/39

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/41
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/41

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/42
cp %{SOURCE12} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/42

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/43
cp %{SOURCE13} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/43

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/47
cp %{SOURCE14} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/47

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/5
cp %{SOURCE15} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/5

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/7
cp %{SOURCE16} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/7

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/9
cp %{SOURCE17} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-parent/9


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/commons/commons-parent/11/commons-parent-11.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-parent/17/commons-parent-17.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-parent/22/commons-parent-22.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-parent/24/commons-parent-24.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-parent/25/commons-parent-25.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-parent/33/commons-parent-33.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-parent/34/commons-parent-34.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-parent/37/commons-parent-37.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-parent/38/commons-parent-38.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-parent/39/commons-parent-39.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-parent/41/commons-parent-41.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-parent/42/commons-parent-42.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-parent/43/commons-parent-43.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-parent/47/commons-parent-47.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-parent/5/commons-parent-5.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-parent/7/commons-parent-7.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-parent/9/commons-parent-9.pom
